/*
 *  Copyright (c) MIT License
 *  2020, Markus Walder (https://github.com/M4rukku)
 */

package org.marukku.ukkonenscs.trienodes;

import org.marukku.ukkonenscs.alphabet.LanguageParameter;

/**
 * Creates {@link UkkonenTrieNode}s, which support the implementation details needed for Ukkonens
 * Linear Time SCS Finder.
 *
 * @author Markus Walder
 * @since 26.12.2020, Sa.
 */
public class UkkonenTrieNodeFactory implements AbstractACNodeFactory<UkkonenTrieNode> {

  /**
   * A simple factory method that takes a set of default parameters and then returns a new Suffix
   * Trie Node supporting Ukkonens' Algorithm based on it.
   *
   * @param parameters  The {@link LanguageParameter} that defines our underlying Alphabet
   * @param isEndOfWord Boolean -Indicates whether this Suffix Trie Node represents the end of a
   *                    word
   * @param parentChar  Character - tells us which character leads to this node from the parent
   * @return Returns a new {@link UkkonenTrieNode} from the given parameters
   */
  @Override
  public UkkonenTrieNode createFromDefaultValues(
      LanguageParameter parameters, boolean isEndOfWord, Character parentChar) {
    return new UkkonenTrieNode(parameters, isEndOfWord, parentChar);
  }
}
