const { defineConfig } = require('@vue/cli-service')
module.exports = {
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/api*": {
        target: "http://localhost:8000",
      }
    }
  }
}
