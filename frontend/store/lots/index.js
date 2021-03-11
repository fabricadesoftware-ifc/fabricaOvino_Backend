export const state = () => ({
  lots: [
    {
      id: '1',
      description: 'Lote 1',
      date: '2020-12-08T17:34:23.200000Z' //Vai vir nesse formato? Transformar nesse -> Tue Dec 08 2020 14:34:23 GMT-0300 (Horário Padrão de Brasília)
    },
    {
      id: '2',
      description: 'Lote 2',
      date: '2021-02-12T18:40:24.200000Z'
    },
    {
      id: '3',
      description: 'Lote 3',
      date: '2021-02-15T16:02:00.200000Z'
    },
    {
      id: '4',
      description: 'Lote 4',
      date: '2021-02-19T10:15:02.200000Z'
    }
  ]
})

export const mutations = {
  loadLots(state, lots) {
    state.lots = lots
  }
}

/*export const actions = {
  async getLots({ commit }) {
    const lots = await this.$axios.$get('/api/v1/lots')
    commit('loadLots', lots)
  }
}*/
