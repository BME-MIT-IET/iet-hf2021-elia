# Build keretrendszer + CI beüzemelése

A feladat célja a CI továbbfejlesztése volt az automatikus SonarCloud-on túl.

A SonarCloud-ot automatikus futás helyett csak GitHub Actions futtatja le.

Ezen felül az Actions Node v12, v14, v15 verziókkal builedeli a projektet.

A tesztek futtatása során a code coverage-et is ellenőrzi, ami a pull requestben is megjelenik.

Végül ESLint (babel parser-t használva) segítségével a kód stílust is ellenőrzi. Ebben az ellenőrzésbe a JSDoc kommentek is beletartoznak. 

Sajnos a feladat elején, a lokális CI branch-et valamért az origin/master-nek vette, és így pár az ehhez a feladathoz kapcsolodó commit oda került, nem látható a pull requestben.

A feladathoz tartozó hiányzó commitok:
- [Add main workflow](https://github.com/BME-MIT-IET/iet-hf2021-elia/commit/85ee9873bd13162bf2becf82edd0aa831aebe6ea)
- [Added package-lock.json for CI](https://github.com/BME-MIT-IET/iet-hf2021-elia/commit/3f475ad5d0002045089bfba7ac44325f26c61441)
- [Removed Node v10 from CI](https://github.com/BME-MIT-IET/iet-hf2021-elia/commit/82603065d6672c60b45ffef8ea9b60645c233d6e)
- [Added properties file for SonarCloud](https://github.com/BME-MIT-IET/iet-hf2021-elia/commit/eb8068c1c1d76030df1376f36afe13ed6de117c3)
- [Formatted main workflow](https://github.com/BME-MIT-IET/iet-hf2021-elia/commit/4e123a1261a75e3a4e2ea96ec0fb9a1c265f8df0)
- [Updated package.json for testing](https://github.com/BME-MIT-IET/iet-hf2021-elia/commit/e8f39fb47f09e50538d4a1e142719943faa0795c)
- [Separated workflow, added Linting](https://github.com/BME-MIT-IET/iet-hf2021-elia/commit/cdd92671a5d2d6153fa8bcdd6cdf9b6150792123)

A kapcsolódó Github issue: [#17](https://github.com/BME-MIT-IET/iet-hf2021-elia/issues/17)