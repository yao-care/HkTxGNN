---
layout: default
title: Ferrous Gluconate
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "FERROUS GLUCONATE"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia", "non-syndromic esophageal malformation", "biotin metabolic disease", "vitamin deficiency disorder"]
description: "Ferrous Gluconate：預測新適應症為Plummer-Vinson 症候群 (Plummer-Vinson syndrome)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ferrous Gluconate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Ferrous Gluconate: Plummer-Vinson 症候群 (Plummer-Vinson syndrome)
{: .text-alpha }

## 一句話總結

Ferrous Gluconate（葡萄糖酸亞鐵）是補鐵藥物，原本用於缺鐵性貧血、早產兒貧血、低色素性貧血等貧血類疾病。
TxGNN 模型預測它可能對 **Plummer-Vinson 症候群 (Plummer-Vinson syndrome)** 有效，但目前**沒有臨床試驗或文獻**直接支持，僅有模型預測與既有臨床知識作為依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Plummer-Vinson 症候群 (Plummer-Vinson syndrome) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5（僅有機轉層面的合理性，無實際研究；依資料編譯結果判定） |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold（列為研究問題，暫不推進） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，鐵劑是補充體內鐵質的藥物，其在缺鐵性貧血中的療效已被廣泛確立。

Plummer-Vinson 症候群的特徵是缺鐵性貧血、吞嚥困難與食道蹼（esophageal web）。補鐵是此病的標準first-line 治療，通常也能改善吞嚥困難，因此模型給出高分與藥物既有的抗缺鐵作用相符。

需要留意的是，這本質上是原有缺鐵性貧血適應症的延伸，而不是真正的新藥物再利用發現。此次資料中沒有相關試驗或文獻，兩者的連結屬於間接推論，建立在既有臨床知識上。

### 其他預測適應症（供參考）

| 排名 | 預測疾病 | 分數 | 評估 |
|------|---------|------|------|
| 2 | 不依賴維生素 B12 與葉酸的體質性巨母紅血球性貧血 | 0.9994 | 此類貧血通常對鐵劑無反應，除非同時缺鐵；高分可能反映網路鄰近性。建議 Hold |
| 3 | 非症候群性食道畸形 | 0.9967 | 結構性先天缺陷，補鐵不會矯正解剖異常；可能源自與 Plummer-Vinson 的關聯。建議 Hold |
| 4 | 生物素代謝疾病 | 0.9942 | 治療以生物素補充為主，鐵劑無明確機轉角色。建議 Hold |
| 5 | 維生素缺乏症 (vitamin deficiency disorder) | 0.9917 | 概念上與營養缺乏相鄰，有 1 個小型試驗但連結間接。列為研究問題 |

---

## 臨床試驗證據

針對首位預測（Plummer-Vinson 症候群）：目前無相關臨床試驗登記。

排名第 5 的預測（維生素缺乏症）有 1 個間接相關試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02233322](https://clinicaltrials.gov/study/NCT02233322) | NA | 完成 | 8 | 先導研究，探討補鐵對體染色體顯性低磷性佝僂症 (ADHR) 中 FGF23 的影響；屬假說產生性證據 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65535 | NUTRYELT CONCENTRATE FOR SOLUTION FOR INFUSION（製造商：BAXTER HEALTHCARE LIMITED） | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病關聯資料，非仿單文字）：消化性潰瘍、遺傳性血色素沉著症、含鐵血黃素沉著症、鐵代謝疾病、Wilson 病、潰瘍性結腸炎、發炎性腸道疾病、溶血性貧血、腸胃炎。
- **藥物交互作用**：共查得 80 筆，以下為部分主要項目：
  - 中度：質子幫浦抑制劑（Omeprazole、Rabeprazole、Lansoprazole、Dexlansoprazole、Pantoprazole、Esomeprazole）、四環素類（Doxycycline、Tetracycline、Minocycline）、Levofloxacin、制酸劑（Magnesium oxide、Calcium carbonate、Aluminum hydroxide、Magaldrate）、Pancrelipase、Sodium sulfate、Triethylenetetramine
  - 輕微：Cimetidine、Zinc sulfate、Zinc acetate

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測 Plummer-Vinson 症候群雖然分數高且臨床上合理，但本質上是缺鐵性貧血適應症的延伸，沒有任何試驗或文獻支持，也不構成新的再利用發現。其餘預測的機轉合理性薄弱。
- 香港許可證為輸注用微量元素濃縮液，許可證未載明適應症與劑型，且仿單層面的安全性資料尚缺，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌、適應症、劑型），確認該產品是否適用於此預測
- 補充作用機轉（MOA）資料
- 檢索 Plummer-Vinson 症候群補鐵治療的文獻與臨床試驗
- 確認給藥途徑相容性（口服鐵劑與目前上市的輸注劑型不同）
- 針對知識圖譜標示的禁忌疾病與主要藥物交互作用，制定風險管理計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

