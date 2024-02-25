# MBR vs. GPT Partitioning

These are the two most common partition types for hard drives.  
1. Master Boot Record (MBR) 
2. GUID Partition Table (GPT).

**MBR:**
- **Age and Compatibility:** MBR dates back to the 1980s, making it the older of the two. It's widely compatible with various operating systems and BIOS-based computers.
- **Partition Limitations:** MBR supports up to four primary partitions or three primary partitions and one extended partition.
- **Maximum Disk Size:** MBR has a maximum disk size limitation of 2TB.
- **Boot Process:** Uses BIOS for booting, which is less flexible and secure compared to UEFI (used by GPT).
- **Boot Partition:** Uses any primary partition for booting, filesystem is irrelevant to the booting process.

**GPT:**
- **Age and Compatibility:** GPT is a newer standard, part of the UEFI specification, offering more advanced features.
- **Partition Limitations:** Allows for virtually unlimited partitions (commonly up to 128 in Windows).
- **Maximum Disk Size:** Supports disks larger than 2TB, theoretically up to 9.4 ZB (zettabytes).
- **Boot Process:** Uses UEFI, which provides more security features (like Secure Boot) and faster boot times.
- **Boot Partition:** Uses a partition that adheres to the EFI specifications, the relevant to a user is using a FAT filesystem containing the bootloader of the system/s.

**Data Recovery:**
- **MBR:** Limited redundancy; if the MBR is corrupted, it could render the disk unusable.
- **GPT:** More robust with multiple copies of the partitioning and boot data across the disk, making it more resilient against data corruption.

**Compatibility and Usage:**
- **MBR:** Best for older systems and smaller drives. Still in use due to its wide compatibility.
- **GPT:** Recommended for modern systems, especially those with UEFI firmware and larger drives.

While MBR is still relevant for older or smaller systems, GPT is the preferred choice for newer systems and larger drives, offering greater flexibility, compatibility with modern technologies, and better data security and resilience.
# Inodes
Inodes are a fundamental concept in the filesystems, they play a crucial role in file management.

**Basic Definition:**
   - An inode (Index Node) is a data structure in a Unix-based filesystem, like those used in Linux. Each inode stores metadata about a file or a directory. This metadata includes attributes like the file's size, ownership, permissions, and timestamps for creation or modification alongside it's location on the hard drive.

**Unique Inode Number:**
   - Every file or directory is associated with an inode. Each inode is identified by a unique inode number within the filesystem. This number acts as a reference point for the actual data in the file or directory.

**Filesystem Structure:**
   - In a typical Linux filesystem (like ext3 or ext4), the total number of inodes is determined at the filesystem's creation. This means the maximum number of files a filesystem can hold is fixed, based on the number of inodes it has.
   - In filesystems like ZFS, the total number of inodes is dynamically created. This prevents writing errors due to exhaustion of inodes

**Inode Contents:**
   - Inodes store various information about files and directories, such as:
     - **File type** (regular file, directory, symlink, etc.)
     - **Permissions** (read, write, execute)
     - **UID** (User ID of the owner)
     - **GID** (Group ID)
     - **Size** of the file
     - **Timestamps** (like last access, last modification)
     - **Links count** (number of hard links)
     - **Pointers array** to the data blocks (where the actual data is stored on the disk).

**Not Storing File Names:**
   - inodes do not store the names of files; they only contain the metadata. The file name and its corresponding inode number are stored in a directory file. This structure allows hard links to exist, where multiple file names can reference the same inode (and thus the same data blocks).

**Managing Inodes:**
   - Commands like `ls -i` in Linux can be used to display the inode number of files. The `df -i` command shows inode usage and availability.
# File system type comparison 

These are windows compatible filesystem, they're available for use in windows by default.

| Filesystem                | FAT32           | NTFS            |
| ------------------------- | --------------- | --------------- |
| **Max File Size**         | 4 GB            | 16 TB           |
| **Max Volume Size**       | 2 TB            | 256 TB          |
| **Filesystem Journaling** | No              | Yes             |
| **Permissions**           | Basic           | Advanced (ACLs) |
| **Used In**               | Removable Media | Windows         |
| **Data Recovery**         | Poor            | Good            |
| **File Compression**      | No              | Yes             |
| **Encryption**            | No              | Yes             |
| **Snapshot Support**      | No              | No              |
| **Timestamp Resolution**  | 2 seconds       | 100 nanoseconds |

These are the most commonly used filesystems for linux machines, now they're mostly used in desktops since they're robust and tested.

| Filesystem                  | EXT1          | EXT2           | EXT3            | EXT4           |
|--------------------------|---------------|----------------|-----------------|----------------|
| **Max File Size**        | 16 GB         | 2 TB           | 2 TB            | 16 TB          |
| **Max Volume Size**      | 2 GB          | 32 TB          | 32 TB           | 1 EB           |
| **Filesystem Journaling**| No            | No             | Yes             | Yes            |
| **Permissions**          | Basic         | Basic          | Basic           | Advanced       |
| **Used In**              | Older Systems | Older Systems  | Linux           | Linux          |
| **Data Recovery**        | Poor          | Moderate       | Good            | Very Good      |
| **File Compression**     | No            | No             | No              | No             |
| **Encryption**           | No            | No             | No              | Yes (since 2009|
| **Snapshot Support**     | No            | No             | No              | No             |
| **Timestamp Resolution** | 1 second      | 1 second       | 1 second        | 1 nanosecond   |

These filesystems have many features that cater to servers, so they're mostly used on them.

| Filesystem                  | XFS             | ZFS              |
|--------------------------|-----------------|------------------|
| **Max File Size**        | 8 EB            | 16 EB            |
| **Max Volume Size**      | 8 EB            | 256 ZB           |
| **Filesystem Journaling**| Yes             | Yes              |
| **Permissions**          | Advanced        | Advanced (ACLs)  |
| **Used In**              | Linux, BSD      | Solaris, FreeBSD |
| **Data Recovery**        | Very Good       | Excellent        |
| **File Compression**     | No              | Yes              |
| **Encryption**           | No              | Yes              |
| **Snapshot Support**     | No              | Yes              |
| **Timestamp Resolution** | 1 nanosecond    | 1 nanosecond     |

- **FAT32:** Widely used for USB drives and memory cards. Limited by file and volume size, lacks journaling and advanced features.
- **NTFS:** Standard for Windows, supports large files, encryption, and has good data recovery options.
- **EXT1/2/3/4:** Linux filesystems with increasing features and capabilities. EXT4 introduces nanosecond timestamps, larger volume size, and encryption.
- **XFS:** Known for high performance, scalability, and efficient allocation of disk space.
- **ZFS:** Advanced filesystem with features like snapshots, copy-on-write, and high storage capacity. Excellent for data integrity and recovery.