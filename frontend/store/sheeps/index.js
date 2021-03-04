export const state = () => ({
  sheeps: []
})

export const mutations = {
  loadSheeps(state, sheeps) {
    state.sheeps = sheeps
  }
}

export const actions = {
  async getSheeps({ commit }) {
    const sheeps = await this.$axios.$get('/api/v1/sheeps')
    commit('loadSheeps', sheeps)
  }
}

export const getters = {
  listSheeps: state => {
    return state.sheeps
  },
  pregnantSheeps: state => {
    return state.sheeps.filter(sheep => sheep.pregnant)
  },
  notPregnantSheeps: state => {
    return state.sheeps.filter(sheep => !sheep.pregnant)
  }
}
