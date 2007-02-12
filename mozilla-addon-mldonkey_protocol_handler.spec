# TODO
# - integrate with browser-common to handle all mozilla based browsers
# - better package name?
Summary:	Mozilla MLdonkey/eMule Protocol Handler
Summary(pl.UTF-8):   Obsługa protokołu MLdonkey/eMule dla Mozilli
%define		vendor_name mldonkey_protocol_handler
Name:		mozilla-addon-%{vendor_name}
Version:	1.7
Release:	0.1
License:	MPL 1.1/GPL 2.0/LGPL 2.1
Group:		X11/Applications/Networking
Source0:	http://www.informatik.uni-oldenburg.de/~dyna/mldonkey/1.7/%{vendor_name}-1.7.xpi
# Source0-md5:	20be3ad138fb9f6bec908591db14585e
Source1:	gen-installed-chrome.sh
URL:		http://www.informatik.uni-oldenburg.de/~dyna/mldonkey/
BuildRequires:	unzip
#Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
#Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
This is a protocol handler for Mozilla and Firefox (see
http://www.mozilla.org/) that forwards some link types to a running
MLdonkey (see http://www.mldonkey.net/) or eMule (see
http://www.emule-project.net/) client. Supported protocols are ed2k:,
magnet: and sig2dat:. For eMule, only ed2k: is supported, of course.

The protocol handler is implemented in JavaScript and should run on
any platform supported by Mozilla or Firefox.

%description -l pl.UTF-8
Ten pakiet zawiera obsługę protokołu dla Mozilli i Firefoksa
(http://www.mozilla.org/) przekazującą niektóre rodzaje odnośników do
działającego klienta MLdonkey (http://www.mldonkey.net/) lub eMule
(http://www.emule-project.net/). Obsługiwane protokoły to ed2k:,
magnet: i sig2dat:. Oczywiście dla eMule obsługinwany jest tylko
ed2k:.

Obsługa protokołu jest zaimplementowana w JavaScripcie i powinna
działać na dowolnej platformie obsługiwanej przez Mozillę lub
Firefoksa.

%prep
%setup -qc
exit 1
install %{SOURCE1} .
./gen-installed-chrome.sh locale chrome/{AD,ca-AD,ca-unix,enigmail-ca-AD}.jar \
	> lang-ca-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{vendor_name}
%{_chromedir}/%{vendor_name}-installed-chrome.txt
