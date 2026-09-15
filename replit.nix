{ pkgs }: {
  deps = [
    pkgs.freetype
    pkgs.glibcLocales
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}