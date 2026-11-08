# -*- coding: utf-8 -*-
"""Jednostavne SVG ilustracije za vodiče (viewBox 0 0 320 240). Bez vanjskih slika."""

MDU = """<svg viewBox="0 0 320 240" role="img" aria-label="Ilustracija: knjiga, lopta i note – aktivnosti za djecu">
<circle cx="160" cy="124" r="104" fill="#fff" opacity=".1"/>
<g class="float"><path d="M70 92c30-14 60-14 88 0v100c-28-14-58-14-88 0z" fill="#fff"/><path d="M162 92c28-14 58-14 88 0v100c-30-14-60-14-88 0z" fill="#E6F2F2"/>
<path d="M158 92v100h4V92z" fill="#12355B" opacity=".35"/><g stroke="#0F6E74" stroke-width="4" stroke-linecap="round" opacity=".55"><path d="M86 112h56M86 128h50M86 144h56M178 112h56M184 128h50M178 144h56"/></g></g>
<g class="float d2"><circle cx="252" cy="70" r="30" fill="#C55A1E" stroke="#fff" stroke-width="4"/><path d="M226 62c16 8 36 8 52 0M226 78c16-8 36-8 52 0M252 40v60" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/></g>
<g class="float d3"><path d="M74 36v40" stroke="#F2A65A" stroke-width="7" stroke-linecap="round"/><path d="M74 36l28-8v34" stroke="#F2A65A" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="64" cy="78" r="11" fill="#F2A65A"/><circle cx="92" cy="64" r="11" fill="#F2A65A"/></g>
<g class="float"><path d="M160 26l7 14 15 2-11 10 3 15-14-7-14 7 3-15-11-10 15-2z" fill="#fff"/></g>
</svg>"""

CDS = """<svg viewBox="0 0 320 240" role="img" aria-label="Ilustracija: škola sa satom – cjelodnevna škola">
<circle cx="160" cy="124" r="104" fill="#fff" opacity=".1"/>
<g class="float"><rect x="74" y="104" width="172" height="104" rx="10" fill="#fff"/><path d="M60 110l100-62 100 62z" fill="#A3262A"/>
<g fill="#E6F2F2"><rect x="92" y="126" width="30" height="26" rx="5"/><rect x="198" y="126" width="30" height="26" rx="5"/><rect x="92" y="164" width="30" height="26" rx="5"/><rect x="198" y="164" width="30" height="26" rx="5"/></g>
<rect x="140" y="160" width="40" height="48" rx="6" fill="#0F6E74"/><circle cx="160" cy="98" r="20" fill="#fff" stroke="#12355B" stroke-width="4"/><path d="M160 86v13l9 6" stroke="#12355B" stroke-width="4" fill="none" stroke-linecap="round"/></g>
<g class="float d2"><g transform="translate(262 52) rotate(35)"><rect x="-8" y="-40" width="16" height="64" rx="3" fill="#F2A65A"/><path d="M-8 24h16l-8 16z" fill="#FBEEE5"/><rect x="-8" y="-46" width="16" height="10" rx="3" fill="#C55A1E"/></g></g>
<g class="float d3"><circle cx="58" cy="60" r="22" fill="#F2A65A"/><path d="M48 60l7 7 13-14" stroke="#12355B" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
</svg>"""

SPORT = """<svg viewBox="0 0 320 240" role="img" aria-label="Ilustracija: lopta, medalja i srce – sport za djecu i mlade">
<circle cx="160" cy="124" r="104" fill="#fff" opacity=".1"/>
<g class="float"><circle cx="150" cy="134" r="64" fill="#fff"/><path d="M150 104l26 19-10 30h-32l-10-30z" fill="#12355B"/>
<g stroke="#12355B" stroke-width="4" fill="none" opacity=".7"><path d="M150 104V72M176 123l28-12M166 153l18 26M134 153l-18 26M124 123l-28-12"/></g></g>
<g class="float d2"><path d="M238 30l14 30M266 30l-14 30" stroke="#0F6E74" stroke-width="8" stroke-linecap="round"/><circle cx="252" cy="80" r="24" fill="#F2A65A" stroke="#fff" stroke-width="4"/><text x="252" y="88" text-anchor="middle" font-family="'Source Sans 3',Arial,sans-serif" font-size="22" font-weight="700" fill="#12355B">1</text></g>
<g class="float d3"><path d="M66 70c-12-14-34-2-26 16 6 12 26 24 26 24s20-12 26-24c8-18-14-30-26-16z" fill="#A3262A" stroke="#fff" stroke-width="3"/></g>
</svg>"""

IKONE = {"mdu": MDU, "cds": CDS, "sport": SPORT}

# ilustracija za slajd na naslovnici: vodič s kvačicama i povećalom
SLAJD = """<svg class="big-scene" viewBox="0 0 320 280" aria-hidden="true"><circle cx="160" cy="145" r="112" fill="#fff" opacity=".08"/>
<g class="float"><rect x="70" y="40" width="160" height="206" rx="16" fill="#fff"/><rect x="70" y="40" width="160" height="44" rx="16" fill="#0F6E74"/><rect x="70" y="66" width="160" height="18" fill="#0F6E74"/>
<text x="150" y="69" text-anchor="middle" font-family="'Source Sans 3',Arial,sans-serif" font-size="16" font-weight="700" fill="#fff" letter-spacing="2">VODIČ</text>
<g stroke-linecap="round" stroke-linejoin="round"><rect x="90" y="104" width="18" height="18" rx="4" fill="#F2A65A"/><path d="M94 113l4 4 7-8" stroke="#12355B" stroke-width="3" fill="none"/><rect x="118" y="109" width="90" height="8" rx="4" fill="#12355B" opacity=".25"/>
<rect x="90" y="138" width="18" height="18" rx="4" fill="#F2A65A"/><path d="M94 147l4 4 7-8" stroke="#12355B" stroke-width="3" fill="none"/><rect x="118" y="143" width="76" height="8" rx="4" fill="#12355B" opacity=".25"/>
<rect x="90" y="172" width="18" height="18" rx="4" fill="#F2A65A"/><path d="M94 181l4 4 7-8" stroke="#12355B" stroke-width="3" fill="none"/><rect x="118" y="177" width="84" height="8" rx="4" fill="#12355B" opacity=".25"/>
<rect x="90" y="206" width="18" height="18" rx="4" fill="none" stroke="#12355B" stroke-width="3" opacity=".4"/><rect x="118" y="211" width="64" height="8" rx="4" fill="#12355B" opacity=".25"/></g></g>
<g class="float d2"><circle cx="236" cy="200" r="34" fill="none" stroke="#F2A65A" stroke-width="12"/><circle cx="236" cy="200" r="28" fill="#fff" opacity=".25"/><path d="M260 226l26 26" stroke="#F2A65A" stroke-width="14" stroke-linecap="round"/></g>
<g class="float d3"><circle cx="64" cy="64" r="22" fill="#C55A1E" stroke="#fff" stroke-width="4"/><text x="64" y="72" text-anchor="middle" font-family="'Source Sans 3',Arial,sans-serif" font-size="20" font-weight="700" fill="#fff">100</text></g>
</svg>"""
