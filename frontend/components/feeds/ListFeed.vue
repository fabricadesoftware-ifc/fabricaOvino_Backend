<template>
  <b-table stripped :data="feeds">
    <template v-slot="props">
      <b-table-column
        v-for="(column, index) in columns"
        :key="index"
        :field="column.field"
<<<<<<< HEAD
        :sortable="column.sortable"
        :label="column.label"
      >
        {{ props.row[column.field] }}
      </b-table-column>
      <b-table-column
=======
        :label="column.label"
        :sortable="column.sortable"
      >
        {{ props.row[column.field] }}
      </b-table-column>
      <b-table-colunm
>>>>>>> origin/Dev-Maria
        custom-key="actions"
        class="is-actions-cell"
        label="Ações"
      >
<<<<<<< HEAD
        <div class="buttons">
          <b-button
            type="is-small is-primary"
            icon-left="pencil"
            @click="loadFeeds(props.row)"
          >
          </b-button>
          <b-button
            type="is-small is-danger"
            icon-left="trash-can-outline"
            @click="confirmRemove(props.row)"
          >
          </b-button>
        </div>
      </b-table-column>
=======
        <b-button
          type="is-small is-primary"
          icon-left="pencil"
          @click="loadFeeds(props.row)"
        ></b-button>
        <b-button
          type="is-small is-danger"
          icon-left="trash-can-outline"
          @click="confirmRemove(props.row)"
        ></b-button>
      </b-table-colunm>
>>>>>>> origin/Dev-Maria
    </template>
  </b-table>
</template>

<script>
export default {
  data() {
    return {
      columns: [
        {
          field: 'id',
          label: '#',
          sortable: true
        },
        {
          field: 'name',
          label: 'Nome',
          sortable: true
        },
        {
          field: 'description',
          label: 'Descrição',
          sortable: true
        }
      ],
      feeds: []
    }
  },
  created() {
    this.carregarFeed()
  },
  methods: {
    async carregarFeed() {
      this.feeds = await this.$axios.$get('/api/v1/feeds')
    },
    loadFeeds() {},
    confirmRemove(feed) {
      this.$buefy.dialog.confirm({
        title: 'Excluir ração?',
        message: 'Você tem certeza que deseja excluir este item?',
        confirmText: 'Excluir',
        cancelText: 'Cancelar',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(feed)
      })
    },
<<<<<<< HEAD

=======
>>>>>>> origin/Dev-Maria
    async remove(feed) {
      const id = feed.id
      const url = `api/v1/feeds/${id}`
      try {
        await this.$axios.$delete(url)
        this.$toasted.global.defaultSuccess()
        this.carregarFeed()
      } catch (err) {
<<<<<<< HEAD
        this.$toast.error(err.response.data)
=======
        this.toast.error(err.response.data)
>>>>>>> origin/Dev-Maria
      }
    }
  }
}
</script>

<style></style>
