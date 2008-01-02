%define name	readseq
%define version	19930201
%define rel	6
%define release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Reads and writes nucleic/protein sequences in various formats
Group:		Sciences/Biology
License:	Public Domain
URL:		http://iubio.bio.indiana.edu/soft/molbio/readseq/
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}.makefile.patch
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
%patch

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


