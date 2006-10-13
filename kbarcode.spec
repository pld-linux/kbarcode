Summary:	A barcode and label printing application for KDE
Summary(pl):	Aplikacja dla KDE do drukowania kodów kreskowych i etykiet
Name:		kbarcode
Version:	2.0.4
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/kbarcode/%{name}-%{version}.tar.gz
# Source0-md5:	86f62225995d9c55a0b8b0bf1dd0e403
Patch0:		kde-common-PLD.patch
URL:		http://www.kbarcode.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBarcode is a barcode and label printing application for Linux and KDE
3. It can be used to print every thing from simple business cards up
to complex labels with several barcodes (e.g. article descriptions).
KBarcode comes with an easy to use WYSIWYG label designer, a setup
wizard, batch import of labels (directly from the delivery note),
thousands of predefined labels, database managment tools and
translations in many languages. Even printing more than 10.000 labels
in one go is no problem for KBarcode. Additionally it is a simply
xbarcode replacement for the creation of barcodes. All major types of
barcodes like EAN, UPC, CODE39 and ISBN are supported.

%description -l pl
KBarcode to aplikacja dla Linuksa i KDE 3 s³u¿±ca do drukowania kodów
kreskowych i etykiet. Mo¿e byæ u¿ywana do wszystkiego, od prostych
wizytówek do z³o¿onych etykiet z kilkoma kodami kreskowymi (np.
opisami artyku³ów). KBarcode zawiera ³atwy w u¿yciu program do
projektowania etykiet, program konfiguracyjny, wsadowy import etykiet
(bezpo¶rednio z opisu dostawy), tysi±ce predefiniowanych etykiet,
narzêdzia do zarz±dzania baz± danych oraz t³umaczenia na wiele
jêzyków. Wydruk nawet 10000 etykiet naraz nie jest problemem dla
KBarcode. Ponadto jest to prosty zamiennik xbarcode do tworzenia kodów
kreskowych. Obs³ugiwane s± wszystkie g³ówne typy kodów kreskowych, jak
EAN, UPC, CODE39 i ISBN.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbarcode
%{_libdir}/kde3/kfile_kbarcode.la
%attr(755,root,root) %{_libdir}/kde3/kfile_kbarcode.so
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/kbarcode
%{_iconsdir}/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/apps/kbarcode.png
%{_datadir}/services/kfile_kbarcode.desktop
