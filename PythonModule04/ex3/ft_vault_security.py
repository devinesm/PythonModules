#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_vault_security.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ipinto-m <ipinto-m@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/19 13:34:36 by ipinto-m           #+#    #+#             #
#   Updated: 2026/06/19 18:51:02 by ipinto-m          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


def secure_archive(filename: str,
                   is_write: int = 0,
                   content: str = "") -> tuple[bool, str]:
    try:
        if (is_write == 0):
            with open(filename, "r") as f:
                return (True, f.read())
        else:
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/non/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", 1, "new content!"))


if __name__ == "__main__":
    main()
