import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _cbce67e6 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))
const _1c8a11e6 = () => interopDefault(import('../pages/admin/index.vue' /* webpackChunkName: "pages/admin/index" */))
const _117c1556 = () => interopDefault(import('../pages/inspire.vue' /* webpackChunkName: "pages/inspire" */))
const _63c06f24 = () => interopDefault(import('../pages/login.vue' /* webpackChunkName: "pages/login" */))
const _615e7ddf = () => interopDefault(import('../pages/logout.vue' /* webpackChunkName: "pages/logout" */))
const _2bd6b526 = () => interopDefault(import('../pages/me.vue' /* webpackChunkName: "pages/me" */))
const _91a5f2a2 = () => interopDefault(import('../pages/admin/breed.vue' /* webpackChunkName: "pages/admin/breed" */))
const _74f28513 = () => interopDefault(import('../pages/admin/category.vue' /* webpackChunkName: "pages/admin/category" */))
const _24bd9b19 = () => interopDefault(import('../pages/admin/pregnancyDiagnosis.vue' /* webpackChunkName: "pages/admin/pregnancyDiagnosis" */))
const _fcd481d4 = () => interopDefault(import('../pages/admin/sheep.vue' /* webpackChunkName: "pages/admin/sheep" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/en/",
    component: _cbce67e6,
    name: "index___en"
  }, {
    path: "/en/admin",
    component: _1c8a11e6,
    name: "admin___en"
  }, {
    path: "/en/inspire",
    component: _117c1556,
    name: "inspire___en"
  }, {
    path: "/en/login",
    component: _63c06f24,
    name: "login___en"
  }, {
    path: "/en/logout",
    component: _615e7ddf,
    name: "logout___en"
  }, {
    path: "/en/me",
    component: _2bd6b526,
    name: "me___en"
  }, {
    path: "/pt/",
    component: _cbce67e6,
    name: "index___pt"
  }, {
    path: "/pt/admin",
    component: _1c8a11e6,
    name: "admin___pt"
  }, {
    path: "/pt/inspire",
    component: _117c1556,
    name: "inspire___pt"
  }, {
    path: "/pt/login",
    component: _63c06f24,
    name: "login___pt"
  }, {
    path: "/pt/logout",
    component: _615e7ddf,
    name: "logout___pt"
  }, {
    path: "/pt/me",
    component: _2bd6b526,
    name: "me___pt"
  }, {
    path: "/en/admin/breed",
    component: _91a5f2a2,
    name: "admin-breed___en"
  }, {
    path: "/en/admin/category",
    component: _74f28513,
    name: "admin-category___en"
  }, {
    path: "/en/admin/pregnancyDiagnosis",
    component: _24bd9b19,
    name: "admin-pregnancyDiagnosis___en"
  }, {
    path: "/en/admin/sheep",
    component: _fcd481d4,
    name: "admin-sheep___en"
  }, {
    path: "/pt/admin/breed",
    component: _91a5f2a2,
    name: "admin-breed___pt"
  }, {
    path: "/pt/admin/category",
    component: _74f28513,
    name: "admin-category___pt"
  }, {
    path: "/pt/admin/pregnancyDiagnosis",
    component: _24bd9b19,
    name: "admin-pregnancyDiagnosis___pt"
  }, {
    path: "/pt/admin/sheep",
    component: _fcd481d4,
    name: "admin-sheep___pt"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
