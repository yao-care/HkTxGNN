---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Enfortumab Vedotin：從尿路上皮癌到麻瘋病

## 一句話總結

Enfortumab vedotin（商品名 Padcev）是靶向 Nectin-4 的抗體藥物複合體（ADC），目前核准用於局部晚期或轉移性尿路上皮癌的治療。
TxGNN 模型預測它可能對**麻瘋病（Leprosy）**有效，預測分數高達 **99.53%**，
然而目前**尚無**臨床試驗或文獻支持這一方向，屬於純模型預測結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尿路上皮癌（局部晚期或轉移性） |
| 預測新適應症 | 麻瘋病（Leprosy） |
| TxGNN 預測分數 | 99.53% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA Data Gap）。根據已知資訊，Enfortumab vedotin 是一種抗體藥物複合體，由靶向 **Nectin-4**（PVRL4，脊髓灰質炎病毒受體相關蛋白 4）的單株抗體，與細胞毒性 payload **MMAE**（monomethyl auristatin E，微管聚合抑制劑）透過可裂解連接子（protease-cleavable linker）組合而成。MMAE 在靶標細胞內釋放後，透過干擾微管聚合誘導細胞週期停滯與凋亡。

麻瘋病（Leprosy）是由麻風分枝桿菌（*Mycobacterium leprae*）引起的慢性感染性疾病，主要侵犯皮膚、黏膜及周圍神經，其致病機轉以免疫逃脫和神經侵犯為主。Nectin-4 在細菌性感染中的直接角色目前尚無明確研究，麻瘋病與 Enfortumab vedotin 原適應症（尿路上皮癌）在生物機轉上的關聯性**難以從現有知識直接解釋**。

TxGNN 模型基於知識圖譜中的間接關聯進行預測，高預測分數可能反映知識圖譜中某些共享蛋白質網絡節點或病理途徑的間接連接。在獲得前臨床生物學證據之前，此預測應視為**假說生成信號**，不具備直接臨床轉化依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗腫瘤靶向 ADC（Antibody-Drug Conjugate）── 含微管抑制劑 MMAE |
| 骨髓抑制風險 | 中至高度（MMAE payload 常見嗜中性白血球減少、貧血、血小板減少） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含白血球分類計數）、肝腎功能、周圍神經病變評估（神經毒性）、血糖（高血糖風險） |
| 處置防護 | 靜脈注射劑型，需依細胞毒性藥物處置規範（Cytotoxic Drug Handling Guidelines）操作，避免皮膚及眼部接觸 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
麻瘋病與 Enfortumab vedotin 之間缺乏已知機轉連結，且無任何臨床試驗或文獻支持，目前僅有 TxGNN 模型預測（L5），不足以推進再利用評估。

值得注意的是，本次 Evidence Pack 中 **HER2 陽性乳癌（Rank 10，預測分數 98.99%）** 已有 **4 個臨床試驗**（含進行中的 Phase 2 研究 NCT04225117、招募中的 NCT07287995 等）及 **4 篇文獻**支持，機轉上更具合理性（Nectin-4 在乳癌等實體腫瘤中有表達），建議優先評估該適應症並另行出具獨立報告。

**若要推進麻瘋病方向需要：**
- Nectin-4 或 MMAE 在麻風分枝桿菌感染模型中的前臨床數據
- 基礎研究：Nectin-4 是否在受感染的皮膚/神經細胞中過度表達
- 作用機轉（MOA）完整資料，以釐清 ADC 在感染性疾病中的可行性（DG002）
- 香港衛生署核准仿單安全性警語與禁忌資料（DG001）
- 評估 Enfortumab vedotin 的 ADC 設計是否適合非腫瘤適應症
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

