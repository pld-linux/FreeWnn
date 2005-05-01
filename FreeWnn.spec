Summary:	FreeWnn Japanese Input System
Summary(pl):	FreeWnn - system wprowadzania znaków japoñskich
Name:		FreeWnn
%define upver	1.1.1
%define alpha	018
Version:	%{upver}a%{alpha}
Release:	1
Epoch:		1
Group:		Applications/System
License:	GPL
Source0:	ftp://ftp.freewnn.org/pub/FreeWnn/alpha/%{name}-%{upver}-a%{alpha}.tar.bz2
# Source0-md5:	e4a56cd7373736c090c6b93a255b950b
Source1:	%{name}.init
Source2:	%{name}-cWnn.init
Source3:	%{name}-tWnn.init
Source4:	%{name}-kWnn.init
Patch0:		%{name}-fhs.patch
Patch1:		%{name}-ja.patch
Patch2:		%{name}-noroot.patch
Patch3:		%{name}-jserverrc-g-jinmei.patch
Patch4:		%{name}-includes.patch
Patch5:		%{name}-reuid.patch
Patch6:		%{name}-manpaths.patch
URL:		http://www.freewnn.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	rpmbuild(macros) >= 1.202
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	setup >= 2.4.1
Conflicts:	wnn6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/FreeWnn

%description
This distribution contains FreeWnn Japanese Input System. FreeWnn is a
network-extensible Kana-to-Kanji conversion system and was jointly
developed and released by the Software Research Group of Kyoto
University Research Institute for Mathematical Science, OMRON
Corporation and Astec, Inc.

%description -l pl
Ten pakiet zawiera system wprowadzania znaków japoñskich FreeWnn. Jest
to, dzia³aj±cy tak¿e przez sieæ, system konwersji Kana do Kanji,
stworzony i rozwijany wspólnie przez Software Research Group z
Institute for Mathematical Science Kyoto University, OMRON Corporation
oraz Astec, Inc.

%package libs
Summary:	Runtime library for FreeWnn
Summary(pl):	Biblioteki wspó³dzielone FreeWnn
Group:		Libraries

%description libs
This package contains the runtime library for running programs with
FreeWnn.

%description libs -l pl
Ten pakiet zawiera biblioteki wspó³dzielone FreeWnn.

%package devel
Summary:	Header files for FreeWnn
Summary(pl):	Pliki nag³ówkowe FreeWnn
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files for building programs with use
FreeWnn.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do budowania programów
u¿ywaj±cych FreeWnn.

%package static
Summary:	Static FreeWnn library
Summary(pl):	Statyczna biblioteka FreeWnn
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of FreeWnn library.

%description static -l pl
Statyczna wersja biblioteki FreeWnn.

%package common
Summary:	Common files for Wnn
Summary(pl):	Wspólne pliki Wnn
Group:		Applications/System
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Provides:	group(wnn)
Provides:	user(wnn)

%description common
FreeWnn-common includes the files you need to run FreeWnn, cWnn or
kWnn.

%description common -l pl
Ten pakiet zawiera wspólne pliki niezbêdne do uruchomienia FreeWnn,
cWnn lub kWnn.

%package -n cWnn
Summary:	cWnn Chinese Input System (version for China)
Summary(pl):	cWnn System wprowadzania znaków chiñskich (wersja dla Chin)
Group:		Applications/System
PreReq:		cWnn-common = %{epoch}:%{version}-%{release}
PreReq:		setup >= 2.4.1-3
Requires(post,preun):	/sbin/chkconfig

%description -n cWnn
This package includes FreeWnn Chinese Input System (version for
China).

%description -n cWnn -l pl
Ten pakiet zawiera system wprowadzania znaków chiñskich FreeWnn w
wersji dla Chin.

%package -n cWnn-common
Summary:	cWnn/tWnn Chinese Input System common files
Summary(pl):	Wspólne pliki systemu wprowadzania znaków chiñskich cWnn/tWnn
Group:		Applications/System
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	cWnn-libs = %{epoch}:%{version}-%{release}

%description -n cWnn-common
This package includes cWnn/tWnn Chinese Input System common files for
China and Taiwan version.

%description -n cWnn-common -l pl
Ten pakiet zawiera pliki wspólne dla wersji chiñskiej i tajwañskiej
systemu wprowadzania znaków chiñskich cWnn/tWnn.

%package -n cWnn-libs
Summary:	cWnn/tWnn runtime library
Summary(pl):	Biblioteka wspó³dzielona cWnn/tWnn
Group:		Libraries

%description -n cWnn-libs
This package contains cWnn/tWnn runtime library.

%description -n cWnn-libs -l pl
Ten pakiet zawiera bibliotekê wspó³dzielon± cWnn/tWnn.

%package -n cWnn-devel
Summary:	Header files for cWnn/tWnn
Summary(pl):	Pliki nag³ówkowe cWnn/tWnn
Group:		Development/Libraries
Requires:	cWnn-libs = %{epoch}:%{version}-%{release}

%description -n cWnn-devel
This package contains the header files for building programs with use
cWnn/tWnn.

%description -n cWnn-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do budowania programów u¿ywaj±cych
cWnn/tWnn.

%package -n cWnn-static
Summary:	Static cWnn/tWnn library
Summary(pl):	Statyczna biblioteka cWnn/tWnn
Group:		Development/Libraries
Requires:	cWnn-devel = %{epoch}:%{version}-%{release}

%description -n cWnn-static
This package contains static version of cWnn/tWnn library.

%description -n cWnn-static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki cWnn/tWnn.

%package -n tWnn
Summary:	tWnn Chinese Input System (version for Taiwan)
Summary(pl):	System wprowadzania znaków chiñskich tWnn (wersja dla Tajwanu)
Group:		Applications/System
PreReq:		cWnn-common = %{epoch}:%{version}-%{release}
PreReq:		setup >= 2.4.1-3
Requires(post,preun):	/sbin/chkconfig

%description -n tWnn
FreeWnn Chinese Input System (version for Taiwan).

%description -n tWnn -l pl
System wprowadzania znaków chiñskich FreeWnn w wersji dla Tajwanu.

%package -n kWnn
Summary:	kWnn Korean Input System
Summary(pl):	System wprowadzania znaków koreañskich kWnn
Group:		Applications/System
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
PreReq:		setup >= 2.4.1-3
Requires(post,preun):	/sbin/chkconfig
Requires:	kWnn-libs = %{epoch}:%{version}-%{release}

%description -n kWnn
FreeWnn Korean Input System.

%description -n kWnn -l pl
System wprowadzania znaków koreañskich FreeWnn.

%package -n kWnn-libs
Summary:	kWnn runtime library
Summary(pl):	Biblioteka wspó³dzielona kWnn
Group:		Libraries

%description -n kWnn-libs
This package contains kWnn runtime library.

%description -n kWnn-libs -l pl
Ten pakiet zawiera bibliotekê wspó³dzielon± kWnn.

%package -n kWnn-devel
Summary:	Header files for kWnn
Summary(pl):	Pliki nag³ówkowe kWnn
Group:		Development/Libraries
Requires:	kWnn-libs = %{epoch}:%{version}-%{release}

%description -n kWnn-devel
This package contains the header files for building programs which use
kWnn.

%description -n kWnn-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do budowania programów u¿ywaj±cych
kWnn.

%package -n kWnn-static
Summary:	Static kWnn library
Summary(pl):	Statyczna biblioteka kWnn
Group:		Development/Libraries
Requires:	kWnn-devel = %{epoch}:%{version}-%{release}

%description -n kWnn-static
This package contains static version of kWnn library.

%description -n kWnn-static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki kWnn.

%prep
#%setup -q -n %{name}-%{upver}-a%{alpha}/Xsi
%setup -q -n %{name}-%{upver}-a017-pl4
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
cd Xsi
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure

%{__make} \
	CDEBUGFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

cd Xsi
%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

# Makefile is missing for these manuals - install manually
for f in atod atof dtoa ; do
	install Wnn/man.en/6.jutil/$f.man $RPM_BUILD_ROOT%{_mandir}/man1/$f.1
done

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/FreeWnn
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/cWnn
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/tWnn
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/kWnn

ln -sf /var/lib/wnn/ja/dic $RPM_BUILD_ROOT%{_sysconfdir}/ja/dic
ln -sf /var/lib/wnn/zh_CN/dic $RPM_BUILD_ROOT%{_sysconfdir}/zh_CN/dic
ln -sf /var/lib/wnn/zh_TW/dic $RPM_BUILD_ROOT%{_sysconfdir}/zh_TW/dic
ln -sf /var/lib/wnn/ko_KR/dic $RPM_BUILD_ROOT%{_sysconfdir}/ko_KR/dic

mv -f Wnn-consortium/dic/README README.Wnn-consortium.dic

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/wnntouch /var/lib/wnn/ja/dic/gerodic/g-jinmei.dic
cd /var/lib/wnn/ja/dic/pubdic
%{_bindir}/wnntouch *.*
/sbin/chkconfig --add FreeWnn
if [ -f /var/lock/subsys/FreeWnn ]; then
	/etc/rc.d/init.d/FreeWnn restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/FreeWnn start\" to start FreeWnn service."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/FreeWnn ]; then
		/etc/rc.d/init.d/FreeWnn stop 1>&2
	fi
	/sbin/chkconfig --del FreeWnn
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post -n cWnn
cd /var/lib/wnn/zh_CN/dic/sys
%{_bindir}/cwnntouch *.*
/sbin/chkconfig --add cWnn
if [ -f /var/lock/subsys/cWnn ]; then
	/etc/rc.d/init.d/cWnn restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/cWnn start\" to start cWnn service."
fi

%preun -n cWnn
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/cWnn ]; then
		/etc/rc.d/init.d/cWnn stop 1>&2
	fi
	/sbin/chkconfig --del cWnn
fi

%post	-n cWnn-libs -p /sbin/ldconfig
%postun	-n cWnn-libs -p /sbin/ldconfig

%post -n tWnn
cd /var/lib/wnn/zh_TW/dic/sys
%{_bindir}/cwnntouch *.*
/sbin/chkconfig --add tWnn
if [ -f /var/lock/subsys/tWnn ]; then
	/etc/rc.d/init.d/tWnn restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/tWnn start\" to start tWnn service."
fi

%preun -n tWnn
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/tWnn ]; then
		/etc/rc.d/init.d/tWnn stop 1>&2
	fi
	/sbin/chkconfig --del tWnn
fi

%post -n kWnn
cd /var/lib/wnn/ko_KR/dic/sys
%{_bindir}/kwnntouch *.*
/sbin/chkconfig --add kWnn
if [ -f /var/lock/subsys/kWnn ]; then
	/etc/rc.d/init.d/kWnn restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/kWnn start\" to start kWnn service."
fi

%preun -n kWnn
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/kWnn ]; then
		/etc/rc.d/init.d/kWnn stop 1>&2
	fi
	/sbin/chkconfig --del kWnn
fi

%post	-n kWnn-libs -p /sbin/ldconfig
%postun	-n kWnn-libs -p /sbin/ldconfig

%pre common
%groupadd -P %{name}-common -g 42 wnn
%useradd -P %{name}-common -u 42 -c "Wnn Service User" -g wnn -s /bin/false wnn

%postun common
if [ "$1" = "0" ]; then
	%userremove wnn
	%groupremove wnn
fi

%files
%defattr(644,root,root,755)
%doc Xsi/Contrib/dic/gerodic/GERODIC Xsi/PubdicPlus/PUBDICPLUS-README
%doc Xsi/Wnn/manual.en
%lang(ja) %doc Xsi/PubdicPlus/PUBDICPLUS-ERRATA Xsi/PubdicPlus/PUBDICPLUS-README.jp
%lang(ja) %doc Xsi/README.Wnn-consortium.dic
%lang(ja) %doc Xsi/Wnn/manual
%attr(754,root,root) /etc/rc.d/init.d/FreeWnn
%attr(755,root,root) %{_bindir}/atod
%attr(755,root,root) %{_bindir}/atof
%attr(755,root,root) %{_bindir}/dtoa
%attr(755,root,root) %{_bindir}/jserver
%attr(755,root,root) %{_bindir}/oldatonewa
%attr(755,root,root) %{_bindir}/wddel
%attr(755,root,root) %{_bindir}/wdreg
%attr(755,root,root) %{_bindir}/wnnkill
%attr(755,root,root) %{_bindir}/wnnstat
%attr(755,root,root) %{_bindir}/wnntouch
%{_mandir}/man1/[ad]*
%lang(ja) %{_mandir}/ja/man[145]/*
%dir /var/lib/wnn/ja
%attr(775,root,wnn) %dir /var/lib/wnn/ja/dic
%attr(775,root,wnn) %dir /var/lib/wnn/ja/dic/*
%attr(664,root,wnn) /var/lib/wnn/ja/dic/*/*
%dir %{_sysconfdir}/ja
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ja/[hjluw]*
%{_sysconfdir}/ja/dic
%{_sysconfdir}/ja/rk
%{_sysconfdir}/ja/rk.vi
%dir %{_sysconfdir}/lt_LN
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/lt_LN/u*
%{_sysconfdir}/lt_LN/rk

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjd.so.*.*
%attr(755,root,root) %{_libdir}/libwnn.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjd.so
%{_libdir}/libjd.la
%attr(755,root,root) %{_libdir}/libwnn.so
%{_libdir}/libwnn.la
%{_includedir}/wnn
%lang(ja) %{_mandir}/ja/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libjd.a
%{_libdir}/libwnn.a

%files common
%defattr(644,root,root,755)
%doc Xsi/CONTRIBUTORS Xsi/ChangeLog.en
%doc Xsi/Xwnmo/manual.en
%lang(ja) %doc Xsi/ChangeLog
%lang(ja) %doc Xsi/Xwnmo/manual
%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/[cs]*
%dir /var/lib/wnn

%files -n cWnn
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/cWnn
%attr(755,root,root) %{_bindir}/cserver
%dir %{_sysconfdir}/zh_CN
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/zh_CN/[cluw]*
%{_sysconfdir}/zh_CN/dic
%{_sysconfdir}/zh_CN/rk
%{_sysconfdir}/zh_CN/rk_p
%{_sysconfdir}/zh_CN/rk_z
%dir /var/lib/wnn/zh_CN
%attr(775,root,wnn) %dir /var/lib/wnn/zh_CN/dic
%attr(775,root,wnn) %dir /var/lib/wnn/zh_CN/dic/*
%attr(664,root,wnn) /var/lib/wnn/zh_CN/dic/*/*
%{_mandir}/man1/cserver.1*

%files -n cWnn-common
%defattr(644,root,root,755)
%doc Xsi/cWnn/manual.en
%lang(ja) %doc Xsi/cWnn/manual
%attr(755,root,root) %{_bindir}/catod
%attr(755,root,root) %{_bindir}/catof
%attr(755,root,root) %{_bindir}/cdtoa
%attr(755,root,root) %{_bindir}/cwddel
%attr(755,root,root) %{_bindir}/cwdreg
%attr(755,root,root) %{_bindir}/cwnnkill
%attr(755,root,root) %{_bindir}/cwnnstat
%attr(755,root,root) %{_bindir}/cwnntouch
%{_mandir}/man1/c[!s]*
%{_mandir}/man4/c*

%files -n cWnn-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcwnn.so.*.*

%files -n cWnn-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcwnn.so
%{_libdir}/libcwnn.la
%{_includedir}/cwnn

%files -n cWnn-static
%defattr(644,root,root,755)
%{_libdir}/libcwnn.a

%files -n tWnn
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/tWnn
%attr(755,root,root) %{_bindir}/tserver
%dir %{_sysconfdir}/zh_TW
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/zh_TW/[cltuw]*
%{_sysconfdir}/zh_TW/dic
%{_sysconfdir}/zh_TW/rk
%{_sysconfdir}/zh_TW/rk_p
%{_sysconfdir}/zh_TW/rk_z
%dir /var/lib/wnn/zh_TW
%attr(775,root,wnn) %dir /var/lib/wnn/zh_TW/dic
%attr(775,root,wnn) %dir /var/lib/wnn/zh_TW/dic/*
%attr(664,root,wnn) /var/lib/wnn/zh_TW/dic/*/*

%files -n kWnn
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kWnn
%attr(755,root,root) %{_bindir}/katod
%attr(755,root,root) %{_bindir}/katof
%attr(755,root,root) %{_bindir}/kdtoa
%attr(755,root,root) %{_bindir}/kserver
%attr(755,root,root) %{_bindir}/kwddel
%attr(755,root,root) %{_bindir}/kwdreg
%attr(755,root,root) %{_bindir}/kwnnkill
%attr(755,root,root) %{_bindir}/kwnnstat
%attr(755,root,root) %{_bindir}/kwnntouch
%dir %{_sysconfdir}/ko_KR
%{_sysconfdir}/ko_KR/dic
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ko_KR/[hkluw]*
%attr(775,root,wnn) %dir /var/lib/wnn/ko_KR/dic
%attr(775,root,wnn) %dir /var/lib/wnn/ko_KR/dic/*
%attr(664,root,wnn) /var/lib/wnn/ko_KR/dic/*/*
%{_sysconfdir}/ko_KR/rk

%files -n kWnn-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkwnn.so.*.*

%files -n kWnn-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkwnn.so
%{_libdir}/libkwnn.la
%{_includedir}/kwnn

%files -n kWnn-static
%defattr(644,root,root,755)
%{_libdir}/libkwnn.a
