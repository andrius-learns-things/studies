const HtmlPlugin = require("html-webpack-plugin");
const path = require("path");

module.exports = {
  entry: [
    "babel-polyfill",
    "react-hot-loader/patch",
    path.join(__dirname, "app", "App.js")
  ],
  output: {
    path: path.resolve(__dirname, "../build"),
    filename: "[hash].[name].js"
  },
  module: {
    rules: [
      {
        enforce: "pre",
        test: /\.jsx?$/,
        use: {
          loader: "eslint-loader"
        },
        exclude: /(node_modules|libs)/
      },
      {
        test: /\.jsx?$/,
        use: ["babel-loader?cacheDirectory"],
        exclude: /(node_modules|libs)/
      },
      {
        test: /\.json$/,
        use: ["json-loader"]
      },
      {
        test: /\.html$/,
        use: [
          {
            loader: "html-loader",
            options: {
              minimize: true
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new HtmlPlugin({
      title: "ClientApp",
      template: "./html/index.html",
      inject: "body"
    })
  ]
};
