var webpackConfig = require("./webpack.config.base");

webpackConfig.module.rules.push({
  test: /\.scss$/,
  use: ["style-loader", "css-loader", "postcss-loader", "sass-loader"]
});

webpackConfig.devServer = {
  host: "0.0.0.0",
  port: 8081,
  proxy: {
    "/api/*": "http://server:8091/"
  }
};

module.exports = webpackConfig;
