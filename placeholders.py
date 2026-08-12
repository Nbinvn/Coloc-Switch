# placeholders.py
# Génère des visuels (avatars, logos, bannières) directement encodés en data URI.
# Aucune requête réseau n'est nécessaire : ces images ne peuvent JAMAIS être "cassées",
# contrairement à des liens hotlinkés vers des sites externes (wiki, flaticon, etc.)
# qui peuvent bloquer le hotlinking à tout moment.

import base64
import hashlib

def _color_for(label: str) -> str:
    """Couleur déterministe (toujours la même pour un même nom) basée sur un hash."""
    h = int(hashlib.md5(label.encode("utf-8")).hexdigest(), 16)
    hue = h % 360
    return f"hsl({hue}, 60%, 42%)"

def _initials(label: str, max_len: int = 3) -> str:
    words = [w for w in label.replace("-", " ").split() if w]
    initials = "".join(w[0] for w in words[:max_len]).upper()
    return initials or "?"

def _to_data_uri(svg: str) -> str:
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"

def avatar_circle(label: str) -> str:
    """Avatar rond avec initiales - pour les personnages MK8 et joueurs."""
    color = _color_for(label)
    initials = _initials(label, 2)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120">
        <circle cx="60" cy="60" r="60" fill="{color}"/>
        <text x="60" y="74" font-size="42" text-anchor="middle" fill="white"
              font-family="Arial, Helvetica, sans-serif" font-weight="700">{initials}</text>
    </svg>'''
    return _to_data_uri(svg)

def logo_shield(label: str) -> str:
    """Écusson stylisé avec initiales - pour les logos d'équipes FC26."""
    color = _color_for(label)
    initials = _initials(label, 3)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="140" viewBox="0 0 120 140">
        <path d="M60 2 L116 22 L116 78 Q116 128 60 138 Q4 128 4 78 L4 22 Z" fill="{color}" stroke="white" stroke-width="3"/>
        <text x="60" y="82" font-size="34" text-anchor="middle" fill="white"
              font-family="Arial, Helvetica, sans-serif" font-weight="700">{initials}</text>
    </svg>'''
    return _to_data_uri(svg)

def track_banner(label: str, difficulty: int = 1) -> str:
    """Bannière colorée pour un circuit MK8 (couleur selon la difficulté)."""
    colors = {1: "#2ecc71", 2: "#f39c12", 3: "#e74c3c"}
    color = colors.get(difficulty, "#7f8c8d")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="120">
        <rect width="160" height="120" rx="10" fill="{color}"/>
        <text x="80" y="66" font-size="30" text-anchor="middle" fill="white"
              font-family="Arial, Helvetica, sans-serif" font-weight="700">🏁</text>
    </svg>'''
    return _to_data_uri(svg)

DEFAULT_PLAYER_AVATAR = avatar_circle("?")
