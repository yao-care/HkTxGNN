---
layout: default
title: Hexachlorophene
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 5
---

# Hexachlorophene
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

# Hexachlorophene：從皮膚消毒（抗菌）到脂溢性角化病

## 一句話總結

Hexachlorophene 是一種歷史悠久的廣效抗菌防腐劑，過去主要用於新生兒皮膚消毒（pHisoHex）及外科刷手製品。
TxGNN 模型預測它可能對**脂溢性角化病 (Seborrheic Keratosis)** 有效，預測分數高達 **99.97%**。
然而，此預測**完全無臨床試驗或文獻支持**，且該藥因已知神經毒性在多國受到嚴格限制。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗菌防腐（皮膚消毒） |
| 預測新適應症 | 脂溢性角化病 (Seborrheic Keratosis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位待補）。根據現有文獻資訊，Hexachlorophene 是一種雙酚類含氯抗菌劑，主要作用機轉為破壞革蘭氏陽性菌（尤其是金黃色葡萄球菌）的細胞膜電子傳遞鏈，1960–1970 年代廣泛用於新生兒全身沐浴消毒及術前外科刷手（商品名 pHisoHex）。

脂溢性角化病（Seborrheic Keratosis）是一種常見的**良性表皮增殖病變**，病理本質為角質細胞過度增殖形成的皮膚突起物，與細菌感染無關，也無已知的微生物參與機轉。

從藥理角度看，Hexachlorophene 的抗菌機轉與脂溢性角化病的角質增殖病理之間**無任何已知藥理關聯**。TxGNN 高分（0.9997）很可能來自知識圖譜中皮膚科節點的高度拓樸共現性（graph topology effect），而非真正的藥理預測信號。此預測缺乏機轉層面的合理性支持，屬圖譜雜訊的可能性較高。

> **補充說明**：TxGNN 排名第 3 的預測適應症「皮膚疾病（Skin Disease）」擁有相對較多的間接歷史證據（2 個臨床試驗、20 篇文獻），主要集中於 Hexachlorophene 在皮膚感染預防（MRSA 去定殖）的歷史應用，但同樣受限於神經毒性安全疑慮，不具現代再利用可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Hexachlorophene 目前**未在香港上市**，無任何核准藥品許可證。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **⚠️ 關鍵安全警示**：根據 Evidence Pack 中的藥理評估，Hexachlorophene 因具有**嚴重神經毒性**（早產兒及新生兒尤為高風險，可導致中樞神經系統空泡化病變），已於 1970 年代被美國 FDA 及多國監管機構嚴格限制使用，目前幾乎僅保留極有限的處方用途。此神經毒性為任何再利用研究的**決定性安全障礙**，在提出替代安全策略前，無法進入 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
脂溢性角化病為良性角質增殖病變，與 Hexachlorophene 的抗菌機轉無藥理關聯；排名第 1 的預測適應症完全無臨床試驗或文獻支持（L5），且該藥因神經毒性已被多國嚴格限制，構成阻斷性安全障礙，現階段不建議推進任何再利用研究。

**若要推進需要：**
- 確認 TxGNN 預測信號是否為圖拓樸效應（建議進行 network topology 分析排除誤報）
- 查詢 DrugBank API 取得完整 MOA 資料（DG002，High 級資料缺口）
- 下載並解析 TFDA/PMDA 仿單，取得完整警語與禁忌資料（DG001，Blocking 級資料缺口）
- 評估是否有安全性更高的候選藥物可達成相同適應症目標，優先於本藥物的再利用探索
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

