---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Finasteride：預測新適應症為Ambras 型全身性先天多毛症 (Ambras type hypertrichosis universalis congenita)（證據等級 L5）。原適應症：良性攝護腺肥大 (benign prostatic hyperplasia)"
---

# Finasteride
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

# Finasteride：從良性攝護腺肥大到先天性多毛症（Ambras 型）

## 一句話總結

Finasteride 原本用於治療**良性攝護腺肥大**。
TxGNN 模型預測它可能對 **Ambras 型全身性先天多毛症 (Ambras type hypertrichosis universalis congenita)** 有效，但目前**沒有臨床試驗、也沒有文獻**直接支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 良性攝護腺肥大 (benign prostatic hyperplasia) |
| 預測新適應症 | Ambras 型全身性先天多毛症 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

註：香港許可證資料中未載明核准適應症文字，原適應症取自 TxGNN 知識圖譜的適應症關聯。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Finasteride 為 type II 5-α 還原酶抑制劑，可減少睪固酮轉變為雙氫睪固酮（DHT），因此用於攝護腺肥大，也與雄性素依賴性毛髮問題（如雄性禿）相關。

然而，Ambras 症候群是一種先天性疾病，與影響 TRPS1 表現的基因體重組有關，並非主要由雄性素驅動。因此藥物機轉與此疾病的關聯**薄弱且間接**。0.9999 的高分僅是計算模型的結果，不能視為療效證據。

其他排名較高的預測（如多毛症、遺傳性毛幹異常）同樣只有部分或推測性的機轉關聯；牙周畸形症候群與 Dandy-Walker 症候群則缺乏合理的藥理機轉，可能是圖譜關聯造成的假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（Ambras 型多毛症），目前無相關文獻。

以下為排名第 2 的預測「多毛症 (hypertrichosis)」的背景文獻，皆為間接證據，沒有任何一篇是 Finasteride 用於多毛症的對照研究：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Ann Dermatol Venereol | 成人多毛症與多毛（hirsutism）的檢查與治療；成人多毛症多為藥物性、代謝性或營養性原因 |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Ther Umsch | 雄性禿、多毛與多毛症的新治療選項回顧 |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Hautarzt | 毛髮疾病的新舊療法；Finasteride 用於男性型禿髮，雷射除毛用於多毛症 |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | 方法學 | Hautarzt | TrichoScan 數位毛髮分析工具介紹（非 Finasteride 療效研究） |

---

## 香港上市資訊

香港共有 20 張有效單方許可證，皆為口服錠劑（資料中未載明劑型與核准適應症文字）。主要許可證如下：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36604 | PROSCAR TAB 5MG | 錠劑 | 未載明 |
| HK-63379 | PROPECIA TABLET 1MG | 錠劑 | 未載明 |
| HK-58465 | FINASTERIDE-TEVA TAB 5MG | 錠劑 | 未載明 |
| HK-64019 | FINASTERIDE-TEVA TABLETS 1MG | 錠劑 | 未載明 |
| HK-63377 | STERCAR TABLETS 5MG | 錠劑 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：肝病、膽囊疾病
- **藥物交互作用**：共查得 100 筆交互作用紀錄，目前等級皆為「未知」，例如 Calcitriol、Doxycycline、Bupropion、Metformin、Omeprazole 等，臨床意義有待確認。
- **懷孕相關風險**：Finasteride 因可能影響男性胎兒生殖器發育而禁用於孕婦。對於先天性畸形類的預測適應症（如 Dandy-Walker 症候群），這點尤其需要注意。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆無臨床試驗，首位預測也無文獻，證據等級僅 L5，且機轉關聯薄弱。
- Ambras 症候群並非雄性素驅動的疾病，Finasteride 的作用機轉難以解釋其療效。

**若要推進需要：**
- 取得詳細的作用機轉資料，並釐清 5-α 還原酶抑制與 TRPS1 相關病理的關聯
- 取得香港仿單的警語與禁忌症資料，完成安全性篩選
- 進行針對先天性多毛症的系統性文獻檢索，確認是否有病例報告
- 若要尋找較合理的再利用方向，建議優先評估雄性素相關的毛髮疾病（如多毛症 hirsutism），而非先天性畸形症候群
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

