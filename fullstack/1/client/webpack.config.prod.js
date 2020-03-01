const webpack = require("webpack");
const webpackConfig = require("./webpack.config.base");

webpackConfig.plugins.push(
  new webpack.optimize.UglifyJsPlugin({
    compress: {
      warnings: false
    }
  }),
  new webpack.BannerPlugin("Client app")
);

module.exports = webpackConfig;
