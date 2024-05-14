# https://nix.dev/tutorials/declarative-and-reproducible-developer-environments
with import <nixpkgs> { };

mkShell {

  # Package names can be found via https://search.nixos.org/packages
    nativeBuildInputs = [
        pkgs.python311Packages.pandas
        pkgs.python311Packages.matplotlib
        pkgs.python311Packages.seaborn
    ];

  NIX_ENFORCE_PURITY = true;

  shellHook = ''
  '';
}
