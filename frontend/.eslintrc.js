let path = require("path");

module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: "babel-eslint",
  },
  extends: ["@nuxtjs", "plugin:prettier/recommended", "prettier/vue", "plugin:i18n-json/recommended"],
  plugins: ["vue"],
  rules: {
    // Disable camelcase lint for properties and destructuring.
    // Makes it easier to work with API parameters and responses.
    camelcase: [
      "error",
      {
        ignoreDestructuring: true,
        properties: "never",
      },
    ],
    "no-console": "warn",
    "no-debugger": "warn",
    "i18n-json/identical-keys": [
      "error",
      {
        filePath: path.resolve("./locales/en/translations.json"),
      },
    ],
    "vue/no-reserved-component-names": "error",
    "vue/no-deprecated-scope-attribute": "error",
    "vue/no-deprecated-slot-attribute": "error",
    "vue/no-deprecated-slot-scope-attribute": "error",
  },
};
