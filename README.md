# rpm-internal-maven

Build a RPM package for the **internal-maven** project.

## RPM build

```
$ docker run --rm -it --volume $(pwd):/specs --volume $(pwd):/output localhost:5000/aallrd/internal-build-rpm --build
[INFO] [14:32:47] RPM spec file: maven.spec
[...]
[SUCCESS] [16:24:33] Binary RPM file(s):
[SUCCESS] [16:24:33] * /root/rpmbuild/RPMS/x86_64/internal-maven-3.5.4-1.el6.x86_64.rpm
[SUCCESS] [16:24:33] Source RPM file(s):
[SUCCESS] [16:24:33] * /root/rpmbuild/SRPMS/internal-maven-3.5.4-1.el6.src.rpm
```

## RPM installation

### Using YUM

```
# Configure the vendor repo on the server
$ cat <<EOF >> /etc/yum.repos.d/vendors.repo

[vendor-internal]
name=internal
baseurl=http://localhost:4000/vendors/internal
enabled=1
gpgcheck=0
proxy=_none_
EOF

# Install the package using Yum
$ yum install -y --disablerepo=* --enablerepo=internal internal-maven
```

### Using RPM

```
$ wget http://localhost:4000/vendors/internal/internal-maven-3.5.4-1.el6.x86_64.rpm
$ yum localinstall -y internal-maven-3.5.4-1.el6.x86_64.rpm
Preparing...   ########################################### [100%]
   1:internal-maven     ########################################### [100%]
```

## Usage

```
$ mvn --version
Apache Maven 3.5.4 (r01de14724cdef164cd33c7c8c2fe155faf9602da; 2013-02-19 08:51:28-0500)
Maven home: /opt/internal/root/opt/maven
Java version: 1.8.0_131, vendor: Oracle Corporation
Java home: /opt/internal/root/usr/java/jdk1.8.0_131/jre
Default locale: en_US, platform encoding: ANSI_X3.4-1968
OS name: "linux", version: "4.4.0-141-generic", arch: "amd64", family: "unix"
```

