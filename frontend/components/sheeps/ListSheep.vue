<template>
  <b-table
    striped
    :data="sheeps"
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
        sortable
        :label="column.label"
      >
        <span v-if="column.field == 'birthday'">
          {{ new Date(props.row[column.field]).toLocaleDateString() }}
        </span>

        <span v-else>
          {{ props.row[column.field] }}
        </span>
      </b-table-column>
      <b-table-column
        field="lactating"
        sortable
        :label="$t('pages.admin.sheep.table.lactating')"
      >
        <span v-if="props.row.lactating">{{ $t('true') }}</span>
        <span v-else>{{ $t('false') }}</span>
      </b-table-column>
      <b-table-column
        field="pregnant"
        sortable
        :label="$t('pages.admin.sheep.table.pregnant')"
      >
        <span v-if="props.row.pregnant">{{ $t('true') }}</span>
        <span v-else>{{ $t('false') }}</span>
      </b-table-column>

      <b-table-column
        field="actions"
        :label="$t('pages.admin.sheep.table.actions')"
      >
        <div class="buttons">
          <b-button
            type="is-small is-warning"
            icon-left="file-document-multiple-outline"
            @click="showHistory(props.row)"
          ></b-button>
          <b-button
            type="is-small is-primary"
            icon-left="pencil"
            @click="editSheep(props.row)"
          ></b-button>
          <b-button
            type="is-small is-danger"
            icon-left="trash-can-outline"
            @click="confirmRemove(props.row)"
          ></b-button>
        </div>
      </b-table-column>
    </template>
  </b-table>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  // props: {
  //   value: {
  //     type: Array
  //   }
  // },
  data() {
    return {
      columns: [
        {
          field: 'earringNumber',
          label: this.$t('pages.admin.sheep.table.earringNumber')
        },
        {
          field: 'breed',
          label: this.$t('pages.admin.sheep.table.breed')
        },
        {
          field: 'category',
          label: this.$t('pages.admin.sheep.table.category')
        },
        {
          field: 'sex',
          label: this.$t('pages.admin.sheep.table.sex')
        },
        {
          field: 'birthday',
          label: this.$t('pages.admin.sheep.table.birthday')
        }
      ]
    }
  },
  computed: {
    ...mapState('sheeps', ['sheeps'])
  },
  created() {
    this.getSheeps()
  },
  methods: {
    ...mapActions('sheeps', ['getSheeps']),
    editSheep(sheep) {
      //console.log(sheep)
      this.$router.push({
        name: `sheeps-detail___${this.$i18n.locale}`,
        params: { sheep }
      })
    },
    showHistory(sheep) {
      this.$router.push({
        name: `sheeps-history___${this.$i18n.locale}`,
        params: { sheep }
      })
    },
    confirmRemove(sheep) {
      this.$buefy.dialog.confirm({
        title: 'Delete Sheep?',
        message:
          'Are you sure to <b>delete</b> this sheep? This action cannot be undone.',
        confirmText: 'Delete',
        cancelText: 'Cancel',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(sheep)
      })
    },
    async remove(sheep) {
      const id = sheep.id
      const url = `/api/v1/sheeps/${id}`
      try {
        await this.$axios.delete(url)
        this.$toasted.global.defaultSuccess()
        this.getSheeps()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    }
  }
}
</script>

<style></style>
