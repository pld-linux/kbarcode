Summary:	A barcode and label printing application for KDE
Name:		kbarcode
Version:	2.0.4
Release:	1
License:	GPL
Group:		Applications
URL:		http://www.kbarcode.net/
Source0:	http://dl.sourceforge.net/kbarcode/%{name}-%{version}.tar.gz
# Source0-md5:	86f62225995d9c55a0b8b0bf1dd0e403
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
