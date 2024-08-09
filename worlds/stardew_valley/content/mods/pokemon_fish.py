from ..game_content import ContentPack
from ..mod_registry import register_mod_content_pack
from ...mods.mod_data import ModNames
from ...data import fish_data
from ...data.harvest import ForagingSource
from ...strings.fish_names import PKMNFish
from ...strings.forageable_names import PKMNForage
from ...strings.season_names import Season
from ...strings.region_names import Region

register_mod_content_pack(ContentPack(
    ModNames.pokemon_fish,
    harvest_sources={
        PKMNForage.corsola: (ForagingSource(seasons=(Season.spring, Season.summer), regions=(Region.beach,)),),
        PKMNForage.corsola_shiny: (ForagingSource(seasons=(Season.spring, Season.summer), regions=(Region.beach,)),),
        PKMNForage.corsola_galarian: (ForagingSource(seasons=(Season.winter,), regions=(Region.beach,)),),
        PKMNForage.mareanie: (ForagingSource(seasons=(Season.spring, Season.summer), regions=(Region.beach,)),),
        PKMNForage.mareanie_shiny: (ForagingSource(seasons=(Season.spring, Season.summer), regions=(Region.beach,)),),
        PKMNForage.pyukumuku: (ForagingSource(seasons=(Season.summer,), regions=(Region.beach,)),),
        PKMNForage.pyukumuku_shiny: (ForagingSource(seasons=(Season.summer,), regions=(Region.beach,)),),
        PKMNForage.sandygast: (ForagingSource(seasons=(Season.summer,), regions=(Region.beach,)),),
        PKMNForage.sandygast_shiny: (ForagingSource(seasons=(Season.summer,), regions=(Region.beach,)),),
        PKMNForage.staryu: (ForagingSource(seasons=(Season.not_winter), regions=(Region.beach,)),),
        PKMNForage.staryu_shiny: (ForagingSource(seasons=(Season.not_winter), regions=(Region.beach,)),),
        PKMNForage.stunfisk: (ForagingSource(seasons=(Season.fall, Season.winter), regions=(Region.beach,)),),
        PKMNForage.wiglett: (ForagingSource(seasons=(Season.spring, Season.summer), regions=(Region.beach,)),),
        PKMNForage.wiglett_shiny: (ForagingSource(seasons=(Season.spring, Season.summer), regions=(Region.beach,)),),
    },
    fishes=(
        fish_data.alomomola,
        fish_data.barboach,
        fish_data.chi_yu,
        fish_data.dratini,
        fish_data.feebas,
        fish_data.frillish_female,
        fish_data.frillish_male,
        fish_data.finneon,
        fish_data.goldeen,
        fish_data.grimer,
        fish_data.horsea,
        fish_data.inkay,
        fish_data.kyogre,
        fish_data.lotad,
        fish_data.lotad_shiny,
        fish_data.luvdisc,
        fish_data.luvdisc_shiny,
        fish_data.magikarp,
        fish_data.magikarp_shiny,
        fish_data.poliwag,
        fish_data.surskit,
        fish_data.tadbulb,
        fish_data.tatsugiri_curly,
        fish_data.tatsugiri_droopy,
        fish_data.tatsugiri_stretchy,
        fish_data.tentacool,
        fish_data.trubbish,
        fish_data.tympole,
        fish_data.tynamo,
        fish_data.wishiwashi,
        fish_data.wooper,
        fish_data.wooper_shiny,
        fish_data.clamperl,
        fish_data.clamperl_shiny,
        fish_data.shellder,
        fish_data.shellder_shiny,
    )
))
