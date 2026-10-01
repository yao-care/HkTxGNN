---
layout: default
title: Trimebutine
parent: 僅模型預測 (L5)
nav_order: 894
evidence_level: L5
indication_count: 2
---

# Trimebutine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Trimebutine：從腸道動力調節藥到偏頭痛

## 一句話總結

Trimebutine 是作用於腸胃道的動力調節藥，香港目前尚無可引用的核准適應症文字。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前**沒有臨床試驗登記**，但有 **4 篇文獻**，其中 1 篇為與 rizatriptan 併用的雙盲隨機試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.64% |
| 證據等級 | L2（僅 1 篇已發表 RCT，且為搭配 triptan 的輔助用藥設計） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Trimebutine 是作用於腸胃道周邊的動力調節藥，
可能透過周邊鴉片類受體與離子通道發揮作用。它在腸胃道疾病中的角色已為人所知，機轉上可能適用於偏頭痛。

偏頭痛發作時常合併胃排空延遲（胃輕癱），這會拖慢口服 triptan 的吸收與起效。
因此研究者推測，加上促進胃腸動力的藥物，可能提升 triptan 的療效與穩定度。
一篇回顧也指出，促動力藥對中樞神經等腸胃道以外的疾病也可能有效。
另一種可能的解釋是腸腦軸（gut-brain axis）相關路徑。

需要注意：這個機轉連結主要是推論，尚未被證實。
另一個預測適應症「伴腦幹先兆的偏頭痛」（分數 99.54%）沒有任何專屬證據，
很可能只是因為在知識圖譜中與偏頭痛節點相近，因此暫不納入評估。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16776704](https://pubmed.ncbi.nlm.nih.gov/16776704/) | 2006 | RCT | Cephalalgia | 雙盲、交叉、安慰劑對照試驗，比較 rizatriptan 單用與 rizatriptan 加 trimebutine 急性治療偏頭痛（所提供摘要未含結果數據） |
| [19220673](https://pubmed.ncbi.nlm.nih.gov/19220673/) | 2009 | Review | J Gastroenterol Hepatol | 回顧促動力藥對腸胃道以外疾病（含中樞神經系統）的療效 |
| [17046449](https://pubmed.ncbi.nlm.nih.gov/17046449/) | 2006 | Review | Lancet | 探討如何提升 triptan 在偏頭痛的效果（無摘要，僅依標題判斷） |
| [16245431](https://pubmed.ncbi.nlm.nih.gov/16245431/) | 2005 | Case report | Pol Merkur Lekarski | 9 歲女童腹型偏頭痛個案，對包含 trimebutine 在內的常用腸胃藥物無改善，與本預測方向無直接支持 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-54719 | SCD TRIMEBUTINE TAB 100MG | LAFARGE CO., LIMITED |
| HK-61307 | POBUTIN TAB 150MG | WAI LUN TRADING CO |
| HK-61960 | TRITIN TABLET 100MG | LSB (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
證據僅有 1 篇與 triptan 併用的 RCT 和少數回顧，沒有登記中的臨床試驗，機轉資料也缺漏。
目前最多只能視為值得研究的問題，尚不足以推進。
此外，香港仿單的警語與禁忌資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症
- 從 DrugBank 補充作用機轉資料
- 取得 PMID 16776704 的全文，確認療效數據與效果大小
- 確認 trimebutine 在香港的核准適應症與劑量，評估用於偏頭痛輔助治療的可行性
- 確認是否有可重複該結果的追加試驗

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

