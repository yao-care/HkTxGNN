---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 5
---

# Griseofulvin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Griseofulvin：從皮癬菌感染到蠅蛆病

## 一句話總結

Griseofulvin 是經典抗真菌抗生素，廣泛用於皮癬菌（Dermatophyte）引起的頭癬、體癬、甲癬等感染。TxGNN 模型預測它可能對**蠅蛆病 (Myiasis)** 有效，然而目前**無任何臨床試驗**，僅有 **1 篇 1970 年的獸醫文獻**作為間接參考，整體證據極為薄弱，且機轉關聯性評估為極弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮癬菌感染（頭癬、體癬、甲癬） |
| 預測新適應症 | 蠅蛆病 (Myiasis) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Griseofulvin 是源自灰黃青黴（*Penicillium griseofulvum*）的抗生素，其主要機轉為干擾真菌微管蛋白（tubulin）的聚合，抑制有絲分裂，對皮癬菌產生抑菌作用。因此，TxGNN 的預測可能源自「anti-tubulin」這個跨物種的共同節點在知識圖譜中的路徑擴散。

然而，蠅蛆病（Myiasis）是由雙翅目（Diptera）蒼蠅幼蟲（蛆）寄生人體組織所致，本質上是**節肢動物感染**，與皮癬菌（真菌）在生物學上差異極大。昆蟲幼蟲的 tubulin 結構與真菌 tubulin 差異顯著，Griseofulvin 對真菌的選擇性抑制安全窗口並不適用於節肢動物，且目前完全缺乏相關體外或體內活性資料支持此推論。**機轉關聯性評分：極弱（0/5）。**

值得注意的是，排名 2–4 的三個蠅蛆病亞型（癤腫性、傷口性、遷移性）TxGNN 分數完全相同（均為 0.9934），強烈提示這些為知識圖譜中同一路徑衍生的批次子節點輸出，而非獨立的正向預測訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Veterinary Review / Case Series | The Veterinary record | 犬貓寄生蟲性皮膚病概述（獸醫文獻；與 Griseofulvin 用於人類蠅蛆病的關聯性待確認） |

---

## 香港上市資訊

Griseofulvin 目前在香港**未上市**，無任何許可證登記記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
蠅蛆病為節肢動物寄生感染，與 Griseofulvin 的抗真菌 tubulin 抑制機轉生物學上幾乎無交集，機轉關聯性極弱（0/5）；現有證據僅限 1 篇 1970 年獸醫文獻（非人體研究），無臨床試驗支持，證據等級為 L5；且多個蠅蛆病亞型分數完全相同，確認為 KG 批次輸出偽訊號。

**若要推進需要：**
- 取得 Griseofulvin 完整 MOA 資料（補足 DG002），確認對節肢動物是否存在任何潛在活性
- 補充香港及其他地區藥品仿單安全性、警語與禁忌資料（補足 DG001）
- 若仍評估此方向，需先完成體外實驗以確認對雙翅目幼蟲的抑制活性，再考慮動物模型驗證（目前幾乎無依據建議直接推進）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

