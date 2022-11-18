const { defineConfig } = require('@vue/cli-service')
module.exports = {
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/api*": {
        target: "http://0.0.0.0:8000/",
      }
    }
  }
}
