const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const LiveReloadPlugin = require('webpack-livereload-plugin');

module.exports = {
  context: __dirname,

  entry: {
    filter: './assets/filter-sitters.jsx'
  },

  output: {
    path: path.resolve('./assets/bundles/'),
    publicPath: '/static/bundles/',
    filename: '[name]-[chunkhash].js',
  },

  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' }),

    new webpack.optimize.CommonsChunkPlugin({
      name: 'commons',
      minChunks: Infinity,
    }),

    ...(process.env.NODE_ENV === 'production'
      ? [
          // removes a lot of debugging code in React
          new webpack.DefinePlugin({
            'process.env': {
              NODE_ENV: JSON.stringify('production'),
            },
            __DEV__: JSON.stringify(false),
          }),

          // minifies your code
          new webpack.optimize.UglifyJsPlugin({
            compressor: {
              warnings: false,
            },
          }),
        ]
      : [
          new LiveReloadPlugin({}),
          new webpack.DefinePlugin({
            __DEV__: JSON.stringify(true),
          }),
        ]),
  ],

  module: {
    rules: [
      {
        test: /\.js[x]*$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: [['es2015', { modules: false }], 'react']
        },
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'style-loader', // creates style nodes from JS strings
          },
          {
            loader: 'css-loader', // translates CSS into CommonJS
          },
          {
            loader: 'sass-loader', // compiles Sass to CSS
          },
        ],
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader', // creates style nodes from JS strings
          },
          {
            loader: 'css-loader', // translates CSS into CommonJS
          },
        ],
      },
    ],
  },
};