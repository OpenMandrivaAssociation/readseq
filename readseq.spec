%define name	readseq
%define version	19930201
%define rel	9
%define release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Reads and writes nucleic/protein sequences in various formats
Group:		Sciences/Biology
License:	Public Domain
URL:		http://iubio.bio.indiana.edu/soft/molbio/readseq/
Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}.makefile.patch
Patch1:		format_arguments_fix.patch
Patch2:		fix_getline.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Readseq is a program for converting among several biosequence file formats,
by D. Gilbert. These formats are currently understood by readseq:

  * ASN.1 format used by NCBI
  * DNAStrider, for common Mac program
  * EMBL, EMBL flatfile format
  * Fitch format, limited use
  * GCG, single sequence format of GCG software
  * GenBank/GB, genbank flatfile format
  * IG/Stanford, used by Intelligenetics and others
  * MSF multi sequence format used by GCG software
  * NBRF format
  * Olsen, format printed by Olsen VMS sequence editor. Input only.
  * PAUP's multiple sequence (NEXUS) format
  * Pearson/Fasta, a common format used by Fasta programs and others
  * Phylip3.2, sequential format for Phylip programs
  * Phylip, interleaved format for Phylip programs (v3.3, v3.4)
  * PIR/CODATA format used by PIR
  * Plain/Raw, sequence data only (no name, document, numbering)
  * Pretty print with various options for nice looking output. Output only.
  * Zuker format, limited use. Input only.

%prep
rm -rf %{buildroot}
%setup
%patch0
%patch1
%patch2

%build
export CFLAGS=$RPM_OPT_FLAGS
make build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Readme Readseq.help Formats
%{_bindir}/%{name}




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 19930201-9mdv2011.0
+ Revision: 614703
- the mass rebuild of 2010.1 packages

* Mon Mar 15 2010 Eric Fernandez <zeb@mandriva.org> 19930201-8mdv2010.1
+ Revision: 519889
- rebuild

* Wed Aug 19 2009 Eric Fernandez <zeb@mandriva.org> 19930201-7mdv2010.0
+ Revision: 417939
- compilation fixes

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 19930201-6mdv2009.0
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Eric Fernandez <zeb@mandriva.org> 19930201-6mdv2008.0
+ Revision: 60316
- rebuild


* Tue Dec 19 2006 Eric Fernandez <zeb@mandriva.org> 19930201-5mdv2007.0
+ Revision: 99617
- Import readseq

* Mon Jun 26 2006 Eric Fernandez <zeb@zebulon.org.uk> 19930201-5mdv2007.0
- rebuild

* Fri Jul 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 19930201-4mdk 
- spec cleanup

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 19930201-3mdk 
- rebuild

* Sat Feb 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 19930201-2mdk
- rebuild

