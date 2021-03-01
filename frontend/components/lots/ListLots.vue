<template>
  <b-table
    striped
    :data="lots"
    paginated
    paginate-position="bottom"
    aria-next-label="Next page"
    aria-previous-label="Previous page"
    aria-page-label="Page"
    aria-current-label="Current page"
    per-page="10"
  >
    <template v-slot="props">
      <b-table-column
        v-for="(column, index) in columns"
        :key="index"
        :field="column.field"
        :sortable="column.sortable"
        :label="column.label"
        ><span v-if="column.field == 'date'">
          {{ new Date(props.row[column.field]).toLocaleDateString() }} -
          {{ new Date(props.row[column.field]).toLocaleTimeString() }}
        </span>
        <span v-else>
          {{ props.row[column.field] }}
        </span>
      </b-table-column>

      <b-table-column
        custom-key="actions"
        class="is-actions-cell"
        :label="$t('pages.lots.table.actions')"
      >
        <div class="buttons">
          <b-button
            type="is-small is-primary"
            icon-left="pencil"
            @click="loadLots(props.row)"
          >
          </b-button>
          <b-button
            type="is-danger"
            class="button is-small"
            icon-left="trash-can-outline"
            @click="confirmRemove(props.row)"
          >
          </b-button>
        </div>
      </b-table-column>
    </template>
  </b-table>
</template>

<script>
import { /*mapActions, */ mapState } from 'vuex'
export default {
  props: {
    checkable: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      columns: [
        {
          field: 'id',
          label: this.$t('pages.lots.table.id'),
          sortable: true
        },
        {
          field: 'description',
          label: this.$t('pages.lots.table.description'),
          sortable: true
        },
        {
          field: 'date',
          label: this.$t('pages.lots.table.date'),
          sortable: true
        }
      ]
    }
  },
  computed: {
    ...mapState('lots', ['lots'])
  },
  /*created() {
    this.getLots()
  },*/
  methods: {
    //...mapActions('lots', ['getLots']),
    loadLots(lots) {
      this.$emit('loadLots', lots)
    },
    confirmRemove(lots) {
      this.$buefy.dialog.confirm({
        title: 'Deletar Lote?',
        message: 'Certeza que deseja excluir esse item?',
        confirmText: 'Delete',
        cancelText: 'Cancel',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(lots)
      })
    },
    async remove(lots) {
      alert('Removendo: ' + lots.description)
      /*const id = lots.id
      const url = `/api/v1/lots/${id}`
      try {
        await this.$axios.delete(url)
        this.$toasted.global.defaultSuccess()
        this.getLots()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }*/
    }
  }
}
</script>

<style></style>
