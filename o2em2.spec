Name: o2em2
Version: 1.51
Release: 2
Source0: http://cznic.dl.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0: o2em2-1.51-optionparsing.patch
Summary: Odyssey2/Videopac+/G7000 emulator
URL: http://o2em2.sf.net/
License: GPLv3
Group: Emulators
BuildRequires: pkgconfig(allegro)

%description
O2em2 is an open source multi-platform Odyssey2 / Videopac+ emulator.
The Odyssey2 (Videopac/Jopac in Europe) was a video game console created
in the late 70s.

O2em2 is a fork of the dead o2em.

%prep
%setup -q
%apply_patches
touch debug.h
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/o2em2
