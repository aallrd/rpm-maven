Name:             internal-maven
Version:          3.6.0
Release:          1%{?dist}
Summary:          Apache Maven is a software project management and comprehension tool.
License:          Apache License v2
URL:              https://maven.apache.org/
Source0:          https://archive.apache.org/dist/maven/maven-3/%{version}/binaries/apache-maven-%{version}-bin.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-buildroot
Requires:         which, internal-oracle-jdk >= 1.8.131
Requires(post):   /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

# RPM configuration
#------------------------
# Don't try to auto provide requires
AutoReqProv:      no
#------------------------

# sysroot's configuration
#------------------------
%define _prefix         /opt/internal/root/opt
%define _exec_prefix    %{_prefix}
%define _mavendir       %{_prefix}/maven
%define _bindir         %{_mavendir}/bin
%define _libdir         %{_mavendir}/lib
%define _confdir        %{_mavendir}/conf
%define _bootdir        %{_mavendir}/boot
#------------------------

%description
Apache Maven is a software project management and comprehension tool.
Based on the concept of a project object model (POM), Maven can
manage a project's build, reporting and documentation from a central
piece of information.

%prep
%setup -qn apache-maven-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mavendir}
# Clean the source archive
rm README.txt
rm NOTICE
rm LICENSE
# Create the environment sourcing script
cat <<EOF >> enable
export PATH="%{_bindir}${PATH:+:${PATH}}"
export M2_HOME="%{_mavendir}"
EOF
# Copy the files in the targeted prefix
cp -r . $RPM_BUILD_ROOT/%{_mavendir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/update-alternatives --install /usr/bin/mvn mvn %{_bindir}/mvn 0

%postun
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove mvn %{_bindir}/mvn
fi

%files
%defattr (-,root,root)

# Files to include
%{_mavendir}/enable
%{_bindir}/m2.conf
%{_bindir}/mvn
%{_bindir}/mvn.cmd
%{_bindir}/mvnDebug
%{_bindir}/mvnDebug.cmd
%{_bindir}/mvnyjp
%{_bootdir}/plexus-classworlds-2.5.2.jar
%{_confdir}/logging/simplelogger.properties
%{_confdir}/settings.xml
%{_confdir}/toolchains.xml
%{_libdir}/animal-sniffer-annotations-1.14.jar
%{_libdir}/animal-sniffer-annotations.license
%{_libdir}/aopalliance-1.0.jar
%{_libdir}/cdi-api-1.0.jar
%{_libdir}/checker-compat-qual-2.0.0.jar
%{_libdir}/checker-compat-qual.license
%{_libdir}/commons-cli-1.4.jar
%{_libdir}/commons-io-2.5.jar
%{_libdir}/commons-lang3-3.8.1.jar
%{_libdir}/error_prone_annotations-2.1.3.jar
%{_libdir}/ext/README.txt
%{_libdir}/guava-25.1-android.jar
%{_libdir}/guice-4.2.1-no_aop.jar
%{_libdir}/j2objc-annotations-1.1.jar
%{_libdir}/jansi-1.17.1.jar
%{_libdir}/jansi-native/README.txt
%{_libdir}/jansi-native/freebsd32/libjansi.so
%{_libdir}/jansi-native/freebsd64/libjansi.so
%{_libdir}/jansi-native/linux32/libjansi.so
%{_libdir}/jansi-native/linux64/libjansi.so
%{_libdir}/jansi-native/osx/libjansi.jnilib
%{_libdir}/jansi-native/windows32/jansi.dll
%{_libdir}/jansi-native/windows64/jansi.dll
%{_libdir}/javax.inject-1.jar
%{_libdir}/jcl-over-slf4j-1.7.25.jar
%{_libdir}/jcl-over-slf4j.license
%{_libdir}/jsr250-api-1.0.jar
%{_libdir}/jsr250-api.license
%{_libdir}/jsr305-3.0.2.jar
%{_libdir}/maven-artifact-3.6.0.jar
%{_libdir}/maven-builder-support-3.6.0.jar
%{_libdir}/maven-compat-3.6.0.jar
%{_libdir}/maven-core-3.6.0.jar
%{_libdir}/maven-embedder-3.6.0.jar
%{_libdir}/maven-model-3.6.0.jar
%{_libdir}/maven-model-builder-3.6.0.jar
%{_libdir}/maven-plugin-api-3.6.0.jar
%{_libdir}/maven-repository-metadata-3.6.0.jar
%{_libdir}/maven-resolver-api-1.3.1.jar
%{_libdir}/maven-resolver-connector-basic-1.3.1.jar
%{_libdir}/maven-resolver-impl-1.3.1.jar
%{_libdir}/maven-resolver-provider-3.6.0.jar
%{_libdir}/maven-resolver-spi-1.3.1.jar
%{_libdir}/maven-resolver-transport-wagon-1.3.1.jar
%{_libdir}/maven-resolver-util-1.3.1.jar
%{_libdir}/maven-settings-3.6.0.jar
%{_libdir}/maven-settings-builder-3.6.0.jar
%{_libdir}/maven-shared-utils-3.2.1.jar
%{_libdir}/maven-slf4j-provider-3.6.0.jar
%{_libdir}/org.eclipse.sisu.inject-0.3.3.jar
%{_libdir}/org.eclipse.sisu.inject.license
%{_libdir}/org.eclipse.sisu.plexus-0.3.3.jar
%{_libdir}/org.eclipse.sisu.plexus.license
%{_libdir}/plexus-cipher-1.7.jar
%{_libdir}/plexus-component-annotations-1.7.1.jar
%{_libdir}/plexus-interpolation-1.25.jar
%{_libdir}/plexus-sec-dispatcher-1.4.jar
%{_libdir}/plexus-utils-3.1.0.jar
%{_libdir}/slf4j-api-1.7.25.jar
%{_libdir}/slf4j-api.license
%{_libdir}/wagon-file-3.2.0.jar
%{_libdir}/wagon-http-3.2.0-shaded.jar
%{_libdir}/wagon-provider-api-3.2.0.jar

# Files to exclude
# none

# Directories owned by this RPM
%dir %{_mavendir}
%dir %{_bootdir}
%dir %{_confdir}
%dir %{_confdir}/logging
%dir %{_bindir}
%dir %{_libdir}
%dir %{_libdir}/jansi-native
%dir %{_libdir}/jansi-native/linux32
%dir %{_libdir}/jansi-native/freebsd32
%dir %{_libdir}/jansi-native/windows32
%dir %{_libdir}/jansi-native/freebsd64
%dir %{_libdir}/jansi-native/osx
%dir %{_libdir}/jansi-native/windows64
%dir %{_libdir}/jansi-native/linux64
%dir %{_libdir}/ext

%changelog
* Thu Jan 17 2019 Antoine Allard <antoine.allard@internal.com>
- Create the RPM

