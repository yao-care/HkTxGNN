---
layout: default
title: Famciclovir
parent: 中證據等級 (L3-L4)
nav_order: 356
evidence_level: L4
indication_count: 5
---

# Famciclovir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Famciclovir：從疱疹病毒感染到感染後神經痛

## 一句話總結

Famciclovir 是一種抗疱疹病毒藥物，在香港已有 8 張上市許可證，但許可證資料未載明核准適應症。
TxGNN 模型預測它可能對**感染後神經痛 (Post-infectious Neuralgia)** 有效。
目前有 **2 個相關臨床試驗**，但都不是以 famciclovir 為試驗藥物，也沒有直接文獻，因此證據仍屬機轉推論層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（機轉資料指向帶狀疱疹等疱疹病毒感染） |
| 預測新適應症 | 感染後神經痛 (Post-infectious Neuralgia) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Famciclovir 在體內會轉換為 penciclovir，抑制水痘帶狀疱疹病毒 (VZV) 的 DNA 聚合酶，進而抑制病毒複製。

帶狀疱疹急性期的病毒複製，與之後發生疱疹後神經痛 (PHN) 有關。如果能及早控制病毒，理論上可能降低神經痛的發生風險或縮短病程。因此，把它預測用於感染後神經痛，在生物學上說得通。

這個關聯是間接的。現有資料中沒有以 famciclovir 為主體、以 PHN 為結果的臨床試驗。0.997 的 TxGNN 分數與這個機轉方向一致，但分數本身不是臨床證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | 不適用 | 尚未招募 | 120 | 以脂質體 bupivacaine 或 ropivacaine 神經阻斷，加脈衝射頻，治療急性帶狀疱疹疼痛。試驗藥物不是 famciclovir，尚無結果 |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | 不適用 | 未知 | 140 | 在帶狀疱疹急性期早期使用 oxycodone，預防 PHN。介入為止痛藥而非抗病毒藥，無法直接支持 famciclovir |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66386 | FAMICOL TABLETS 250MG | LAFARGE CO., LIMITED |
| HK-39905 | FAMVIR TAB 125MG | PRUDENTLINK LIMITED |
| HK-57504 | PMS-FAMCICLOVIR TAB 250MG | TRENTON-BOMA LTD |
| HK-39023 | FAMVIR TAB 250MG | PRUDENTLINK LIMITED |
| HK-58557 | APO-FAMCICLOVIR TAB 125MG | HIND WING CO LTD |

以上列出 5 張主要許可證，共 8 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有 TxGNN 預測和間接的機轉推論。
- 兩個相關試驗都不是以 famciclovir 為介入，也沒有直接支持的文獻。
- 香港衛生署仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症。
- 查詢 DrugBank 取得作用機轉資料。
- 搜尋並評讀 famciclovir 用於帶狀疱疹急性期、以 PHN 發生率或持續時間為結果的研究，包括 RCT 與系統性回顧。
- 釐清 famciclovir 早期抗病毒治療能否降低 PHN 風險，再決定是否值得設計臨床研究。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

