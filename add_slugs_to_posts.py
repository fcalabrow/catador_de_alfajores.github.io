#!/usr/bin/env python3
"""
Script para agregar el campo 'slug' al front matter de los posts.
Extrae el slug del nombre del archivo (después de la fecha).
"""

import re
from pathlib import Path

POSTS_DIR = Path("_posts")

def extract_slug_from_filename(filename):
    """Extrae el slug del nombre del archivo."""
    # Formato: YYYY-MM-DD-slug.md
    match = re.match(r'\d{4}-\d{2}-\d{2}-(.+)\.md', filename)
    if match:
        return match.group(1)
    return None

def add_slug_to_post(file_path):
    """Agrega el campo slug al front matter del post."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si ya tiene slug
        if 'slug:' in content:
            return False
        
        # Extraer slug del nombre del archivo
        slug = extract_slug_from_filename(file_path.name)
        if not slug:
            return False
        
        # Buscar el front matter (entre --- y ---)
        front_matter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(front_matter_pattern, content, re.DOTALL)
        
        if not match:
            return False
        
        front_matter = match.group(1)
        body = content[match.end():]
        
        # Agregar slug después de title o date
        if 'date:' in front_matter:
            # Insertar después de date
            front_matter = re.sub(
                r'(date:.*\n)',
                r'\1slug: ' + slug + '\n',
                front_matter
            )
        elif 'title:' in front_matter:
            # Insertar después de title
            front_matter = re.sub(
                r'(title:.*\n)',
                r'\1slug: ' + slug + '\n',
                front_matter
            )
        else:
            # Agregar al final del front matter
            front_matter += '\nslug: ' + slug
        
        # Reconstruir el contenido
        new_content = '---\n' + front_matter + '\n---\n' + body
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"  ⚠️  Error procesando {file_path.name}: {e}")
        return False

def main():
    print("🔧 Agregando slugs a los posts...")
    
    posts_updated = 0
    for post_file in POSTS_DIR.glob("*.md"):
        if add_slug_to_post(post_file):
            print(f"  ✓ {post_file.name}")
            posts_updated += 1
    
    print(f"\n✅ {posts_updated} posts actualizados con slug")

if __name__ == "__main__":
    main()

