---
layout: default
title: Fusidic Acid
parent: 中證據等級 (L3-L4)
nav_order: 338
evidence_level: L4
indication_count: 5
---

# Fusidic Acid
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

# Fusidic Acid：從細菌感染治療到 Exposure Keratitis

## 一句話總結

Fusidic acid 是一種窄效抗菌藥物，在多個國家已核准用於細菌性皮膚感染及眼部感染（如結膜炎）的治療。
TxGNN 模型預測它可能對 **Exposure Keratitis（暴露性角膜炎）** 有效，
目前有 **0 個臨床試驗**和 **1 篇文獻**支持這個方向，整體證據尚不充分。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性皮膚感染、眼部細菌感染（多國核准，香港未上市） |
| 預測新適應症 | Exposure Keratitis（暴露性角膜炎） |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理資訊，Fusidic acid 是一種固醇酸類（steroid acid）抗生素，透過抑制細菌蛋白質合成延伸因子 EF-G，阻斷核糖體易位步驟，對 *Staphylococcus aureus*（包括部分 MRSA 株）具高效抑菌活性，窄效且不易與其他類別產生交叉抗藥性。

Fusidic acid 眼用製劑（如 1% 眼藥水）在歐洲及亞洲多國已核准用於細菌性結膜炎，理論上對眼表細菌感染具涵蓋力。然而，**Exposure keratitis（暴露性角膜炎）的本質是機械性病變**，肇因為眼瞼閉合不全（如顏面神經麻痺、突眼症、外翻術後），並非原發性細菌感染；其主要治療為潤滑點眼液、眼瞼縫合或矯正手術。

在此情境下，抗生素的角色僅限於**預防繼發性細菌感染**，並非主要治療機轉。TxGNN 高分可能來自知識圖譜中「眼科抗生素」與「角膜疾病」廣義節點的結構性關聯，臨床可行性需謹慎評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case Series | Cornea | Tsukamurella 機會性感染相關眼科病變最大案例系列，涵蓋臨床表現、危險因子及治療結果，與 fusidic acid 用於 exposure keratitis 無直接關聯 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Exposure keratitis 屬機械性角膜病變，非細菌感染性疾病，抗生素僅作輔助預防角色。現有證據等級僅達 L4（前臨床/機轉研究層），且香港目前無任何許可登記，整體再利用基礎薄弱，不建議優先推進此適應症。

**若要推進需要：**
- 確認 fusidic acid 完整 MOA 資料及眼用製劑安全性數據（現為 Data Gap）
- 蒐集 fusidic acid 眼部製劑預防繼發感染的前瞻性臨床研究
- 香港上市前需完成藥品許可登記全程申請（目前為零登記）
- **建議優先評估更具證據基礎的預測適應症**：
  - **Rank 5：Post-bacterial disorder / ABSSSI**（NCT02570490，已完成 Phase 3 RCT，716 例，口服 fusidic acid 鈉鹽 vs. linezolid），證據等級 L2，決策建議 Proceed with Guardrails
  - **Rank 3：Otitis externa（外耳炎）**，有機轉合理性（S. aureus 主要病原），可作為研究問題進一步探索
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

