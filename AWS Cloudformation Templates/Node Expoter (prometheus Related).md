This installs node-exporter
you will need to add both dns and port 9100 to prometheus instance manually
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
          useradd --no-create-home node_exporter
          wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz
          tar xzf node_exporter-1.0.1.linux-amd64.tar.gz
          cp node_exporter-1.0.1.linux-amd64/node_exporter /usr/local/bin/node_exporter
          rm -rf node_exporter-1.0.1.linux-amd64.tar.gz node_exporter-1.0.1.linux-amd64
          echo "[Unit]
          Description=Prometheus Node Exporter Service
          After=network.target

          [Service]
          User=node_exporter
          Group=node_exporter
          Type=simple
          ExecStart=/usr/local/bin/node_exporter

          [Install]
          WantedBy=multi-user.target" > /etc/systemd/system/node-exporter.service
          systemctl daemon-reload
          systemctl enable node-exporter
          systemctl start node-exporter
      Tags:
        - Key: Name
          Value: Node Exporter Instance
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