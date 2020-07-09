export const state = () => ({
  categories: []
})

export const mutations = {
  loadCategories(state, categories) {
    state.categories = categories
  }
}

export const actions = {
  async getCategories({ commit }) {
    const categories = await this.$axios.$get('/api/v1/categories')
    commit('loadCategories', categories)
  }
}
