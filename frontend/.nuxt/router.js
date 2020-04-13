import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _cbce67e6 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))
const _117c1556 = () => interopDefault(import('../pages/inspire.vue' /* webpackChunkName: "pages/inspire" */))
const _91a5f2a2 = () => interopDefault(import('../pages/admin/breed.vue' /* webpackChunkName: "pages/admin/breed" */))
const _74f28513 = () => interopDefault(import('../pages/admin/category.vue' /* webpackChunkName: "pages/admin/category" */))

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
    path: "/en/inspire",
    component: _117c1556,
    name: "inspire___en"
  }, {
    path: "/pt/",
    component: _cbce67e6,
    name: "index___pt"
  }, {
    path: "/pt/inspire",
    component: _117c1556,
    name: "inspire___pt"
  }, {
    path: "/en/admin/breed",
    component: _91a5f2a2,
    name: "admin-breed___en"
  }, {
    path: "/en/admin/category",
    component: _74f28513,
    name: "admin-category___en"
  }, {
    path: "/pt/admin/breed",
    component: _91a5f2a2,
    name: "admin-breed___pt"
  }, {
    path: "/pt/admin/category",
    component: _74f28513,
    name: "admin-category___pt"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
