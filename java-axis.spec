# TODO
#  - castor is needed by axis-1.2.1-0.2jpp.1.noarch
#  - package axis2, axis is obsolete. see NOTE below.
#  - build samples
#  - package war app
# NOTE
#  - it won't compile with java 1.6. see:
#    https://fcp.surfsite.org/modules/newbb/viewtopic.php?topic_id=55862&viewmode=flat&order=ASC&start=20


%define		archivever %(echo %{version} | tr . _)
%define		srcname	axis
Summary:	A SOAP implementation in Java
Summary(pl.UTF-8):	Implementacja SOAP w Javie
Name:		java-axis
Version:	1.4
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://ws.apache.org/axis/dist/%{archivever}/%{srcname}-src-%{archivever}.tar.gz
# Source0-md5:	541efc07c135c4dc7f0e1c9573aec8e1
Source1:	%{srcname}-build.xml
Patch0:		%{srcname}-classpath.patch
Patch1:		%{srcname}-missing_xsd.patch
URL:		http://ws.apache.org/axis/
# BuildRequires:	jimi
# BuildRequires:	jms
BuildRequires:	ant >= 1.6
BuildRequires:	ant-nodeps
BuildRequires:	java(jaf)
BuildRequires:	java(javamail)
BuildRequires:	java(jsse)
BuildRequires:	java-commons-discovery
BuildRequires:	java-commons-httpclient
BuildRequires:	java-commons-logging
BuildRequires:	java-commons-net
BuildRequires:	java-junit
BuildRequires:	java-log4j
BuildRequires:	java-oro
BuildRequires:	jdk <= 1.5
BuildRequires:	java-wsdl4j
BuildRequires:	java-xalan
BuildRequires:	java-xerces
BuildRequires:	java-xml-commons
BuildRequires:	java-xmlbeans
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	servletapi5
Requires:	java(jaf)
Requires:	java(javamail)
Requires:	java(jsse)
Requires:	java-commons-discovery
Requires:	java-commons-httpclient
Requires:	java-commons-logging
Requires:	java-commons-net
Requires:	java-log4j
Requires:	java-oro
Requires:	java-wsdl4j
Requires:	java-xalan
Requires:	java-xerces
Requires:	java-xml-commons
Requires:	java-xmlbeans
Requires:	jpackage-utils
Requires:	servletapi5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache AXIS is an implementation of the SOAP ("Simple Object Access
Protocol") submission to W3C.

From the draft W3C specification:

SOAP is a lightweight protocol for exchange of information in a
decentralized, distributed environment. It is an XML based protocol
that consists of three parts: an envelope that defines a framework for
describing what is in a message and how to process it, a set of
encoding rules for expressing instances of application-defined
datatypes, and a convention for representing remote procedure calls
and responses.

This project is a follow-on to the Apache SOAP project.

%description -l pl.UTF-8
Apache AXIS to implementacja SOAP ("Simple Object Access Protocol")
przekazanego do W3C.

Z projektu specyfikacji W3C:

SOAP to lekki protokół do wymiany informacji w scentralizowanym,
rozproszonym środowisku. Jest to protokół oparty na XML-u, składający
się z trzech części: koperty definiującej szkielet do opisu zawartości
i sposobu przetwarzania komunikatu, zbioru reguł kodowania do
wyrażania instancji typów danych zdefiniowanych w aplikacji oraz
konwencji reprezentowania zdalnych wywołań procedur i odpowiedzi.

Ten projekt jest następcą projektu Apache SOAP.

%package javadoc
Summary:	Javadoc for %{srcname}
Summary(pl.UTF-8):	Dokumentacja javadoc dla pakietu %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc dla pakietu %{srcname}.

%package manual
Summary:	Manual for %{srcname}
Summary(pl.UTF-8):	Podręcznik do pakietu %{srcname}
Group:		Development/Languages/Java

%description manual
Documentation for %{srcname}.

%description manual -l pl.UTF-8
Podręcznik do pakietu %{srcname}.

%prep
%setup -q -n %{srcname}-%{archivever}

# Remove provided binaries
find -name '*.jar' | xargs rm -v
find -name '*.class' | xargs rm -v

%patch0 -p1
%patch1 -p1

cp %{SOURCE1} build.xml

%build
export JAVA_HOME=%{java_home}
echo $JAVA_HOME

activation_jar=$(find-jar activation)
commons_logging_jar=$(find-jar commons-logging)
commons_discovery_jar=$(find-jar commons-discovery)
commons_httpclient_jar=$(find-jar commons-httpclient)
commons_net_jar=$(find-jar commons-net)
log4j_core_jar=$(find-jar log4j)
jsse_jar=$(find-jar jsse)
junit_jar=$(find-jar junit)
mailapi_jar=$(find-jar mail)
regexp_jar=$(find-jar oro)
servlet_jar=$(find-jar servletapi5)
tools_jar=$(find-jar tools)
wsdl4j_jar=$(find-jar wsdl4j)
xalan_jar=$(find-jar xalan)
xerces_jar=$(find-jar xerces-j2)
xercesImpl_jar=$(find-jar xercesImpl)
xml_apis_jar=$(find-jar xml-commons-apis)
xmlParsersAPIs_jar=$(find-jar xerces-j2)
xmlbeans_jar=$(find-jar xmlbeans)
%{!?with_java_sun:libgcj_jar=$(find-jar libgcj)}

#httpunit_jar=$(find-jar httpunit)
#xmlunit_jar=$(find-jar xmlunit)
#jimi_jar=$(find-jar jimi)

CLASSPATH=$wsdl4j_jar:$commons_logging_jar:$commons_discovery_jar

export CLASSPATH

%ant dist \
	-Dactivation.jar=$activation_jar \
	-Dcommons-logging.jar=$commons_logging_jar \
	-Dcommons-discovery.jar=$commons_discovery_jar \
	-Dcommons-httpclient.jar=$commons_httpclient_jar \
	-Dcommons-net.jar=$commons_net_jar \
	-Dlog4j-core.jar=$log4j_core_jar \
	-Djsse.jar=$jsse_jar \
	-Djunit.jar=$junit_jar \
	-Dmailapi.jar=$mailapi_jar \
	-Dregexp.jar=$regexp_jar \
	-Dservlet.jar=$servlet_jar \
	-Dtools.jar=$tools_jar \
	-Dwsdl4j.jar=$wsdl4j_jar \
	-Dxalan.jar=$xalan_jar \
	-Dxerces.jar=$xerces_jar \
	-DxercesImpl.jar=$xercesImpl_jar \
	-Dxml-apis.jar=$xml_apis_jar \
	-DxmlParsersAPIs.jar=$xmlParsersAPIs_jar \
	-Dxmlbeans.jar=$xmlbeans_jar \
	%{!?with_java_sun:-Dsun.boot.class.path="$libgcj_jar:[-org.w3c.dom/*]"}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}/%{srcname}

cd build/lib
install axis.jar axis-ant.jar saaj.jar jaxrpc.jar \
	$RPM_BUILD_ROOT%{_javadir}/%{srcname}
cd -

cd $RPM_BUILD_ROOT%{_javadir}/%{srcname}
for jar in *.jar ; do
	vjar=$(echo $jar | sed s+.jar+-%{version}.jar+g)
	mv $jar $vjar
	ln -fs $vjar $jar
done
cd -

### Javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE README release-notes.html changelog.html
%dir %{_javadir}/%{srcname}
%{_javadir}/%{srcname}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}

%files manual
%defattr(644,root,root,755)
%doc docs/*
