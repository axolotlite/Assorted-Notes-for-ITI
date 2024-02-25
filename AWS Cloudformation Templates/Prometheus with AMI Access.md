This instance uses an access key and secret access key created by aws AMI to scrape ec2 instances
you'll need to parameterize this before launching it.
```
Description: Template to create an EC2 instance, enable SSH access to the instance and open ports for promethius
Parameters: 
  KeyName: 
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instance
    Type: 'AWS::EC2::KeyPair::KeyName'
    ConstraintDescription: Provide the name of an existing SSH key pair 
  AMI:
    Description:  name of AMI used 
    Type: String
  IAMAccessID:
    Description:  Access Key Id of Prometheus user
    Type: String
  IAMSecretKey:
    Description:  Secret Access Key of Prometheus user
    Type: String
Resources: 
  MyEC2Instance: 
    Type: 'AWS::EC2::Instance'
    Properties: 
      InstanceType: t2.micro
      ImageId: !Ref AMI
      SecurityGroups:
      - !Ref InstanceSecurityGroup        
      KeyName: !Ref KeyName
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          sudo useradd --no-create-home prometheus
          sudo mkdir /etc/prometheus
          sudo mkdir /var/lib/prometheus
          wget https://github.com/prometheus/prometheus/releases/download/v2.19.0/prometheus-2.19.0.linux-amd64.tar.gz
          tar xvfz prometheus-2.19.0.linux-amd64.tar.gz

          sudo cp prometheus-2.19.0.linux-amd64/prometheus /usr/local/bin
          sudo cp prometheus-2.19.0.linux-amd64/promtool /usr/local/bin/
          sudo cp -r prometheus-2.19.0.linux-amd64/consoles /etc/prometheus
          sudo cp -r prometheus-2.19.0.linux-amd64/console_libraries /etc/prometheus

          sudo cp prometheus-2.19.0.linux-amd64/promtool /usr/local/bin/
          rm -rf prometheus-2.19.0.linux-amd64.tar.gz prometheus-2.19.0.linux-amd64
          echo "global:
            scrape_interval: 15s
            external_labels:
              monitor: 'prometheus'
          scrape_configs:
            - job_name: 'prometheus'
              static_configs:
                - targets: ['localhost:9090']
            - job_name: 'node'
              ec2_sd_configs:
                - region: us-east-1
                  access_key: ${IAMAccessID}
                  secret_key: ${IAMSecretKey}
                  port: 9100

          " > /etc/prometheus/prometheus.yml
          echo "[Unit]
          Description=Prometheus
          Wants=network-online.target
          After=network-online.target

          [Service]
          User=prometheus
          Group=prometheus
          Type=simple
          ExecStart=/usr/local/bin/prometheus \
              --config.file /etc/prometheus/prometheus.yml \
              --storage.tsdb.path /var/lib/prometheus/ \
              --web.console.templates=/etc/prometheus/consoles \
              --web.console.libraries=/etc/prometheus/console_libraries

          [Install]
          WantedBy=multi-user.target" > /etc/systemd/system/prometheus.service
          chown prometheus:prometheus /etc/prometheus
          chown prometheus:prometheus /usr/local/bin/prometheus
          chown prometheus:prometheus /usr/local/bin/promtool
          chown -R prometheus:prometheus /etc/prometheus/consoles
          chown -R prometheus:prometheus /etc/prometheus/console_libraries
          chown -R prometheus:prometheus /var/lib/prometheus
          systemctl daemon-reload
          systemctl enable prometheus
          prometheus --config.file=/etc/prometheus/prometheus.yml
      Tags:
        - Key: Name
          Value: Prometheus Instance
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 9090
          ToPort: 9090
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 9093
          ToPort: 9093
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 9100
          ToPort: 9100
          CidrIp: 0.0.0.0/0
Outputs: 
  InstanceID: 
    Description: The Instance ID
    Value: !Ref MyEC2Instance 
  InstanceIPV4:
    Description: The Instance IP
    Value: !GetAtt MyEC2Instance.PublicDnsName
```