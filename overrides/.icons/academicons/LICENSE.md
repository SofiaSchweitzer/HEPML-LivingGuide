# Vendored Academicons icons

`orcid.svg` and `inspire.svg` are taken from
[Academicons](https://github.com/jpswalsh/academicons) by James Walsh, licensed
under the [SIL Open Font License 1.1](https://scripts.sil.org/OFL).

They are vendored rather than loaded from a CDN so that author identifiers keep
working offline and in a repo mirror, and so the glyphs inherit the theme's link
color instead of arriving with the CDN's own stylesheet.

Changes from upstream: the Inkscape and RDF metadata blocks are stripped, the
`width`/`height` attributes are dropped so Material can size the glyph, `fill` is
omitted so it inherits `currentColor`, and `fill-rule="evenodd"` is set explicitly
so the letter counters stay knocked out.

To vendor another one:

    npm pack academicons && tar xzf academicons-*.tgz
    # take the `d` attribute out of package/svg/<name>.svg and wrap it as above
