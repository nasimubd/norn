const fs = require("node:fs");
const version = process.argv[2];
if (!version || !/^\d+\.\d+\.\d+$/.test(version)) throw new Error("expected a semantic version");
fs.writeFileSync("VERSION", `${version}\n`);
const path = "pyproject.toml";
const source = fs.readFileSync(path, "utf8");
const updated = source.replace(/^version = ".*"$/m, `version = "${version}"`);
if (source === updated) throw new Error("pyproject.toml version field not found");
fs.writeFileSync(path, updated);
