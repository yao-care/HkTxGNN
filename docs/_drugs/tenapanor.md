---
layout: default
title: Tenapanor
parent: 僅模型預測 (L5)
nav_order: 856
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tenapanor：預測新適應症為念珠菌感染 (Candidiasis)（證據等級 L5）。原適應症：香港許可證未載明（參考美國 FDA：便秘型腸躁症 IBS-C"
monitor_inn: "Tenapanor"
predicted_indications: ["candidiasis", "adrenocortical insufficiency", "familial adrenal hypoplasia with absent pituitary luteinizing hormone", "primary cutaneous T-cell lymphoma", "Stevens-Johnson syndrome", "PAGOD syndrome", "aphthous stomatitis", "46,XY disorder of sex development", "Stevens-Johnson syndrome/toxic epidermal necrolysis overlap syndrome", "Crohn's colitis"]
---

# Tenapanor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Tenapanor：從香港已核准用途到念珠菌感染（候選預測）

## 一句話總結

Tenapanor 是一種腸道局部作用、全身吸收極低的 NHE3（鈉/氫交換體 3）抑制劑，已在美國核准用於便秘型腸躁症（IBS-C），以及透析病人的高磷血症。
TxGNN 模型預測它可能對**念珠菌感染 (Candidiasis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明（參考美國 FDA：便秘型腸躁症 IBS-C；透析病人高磷血症） |
| 預測新適應症 | 念珠菌感染 (Candidiasis) |
| TxGNN 預測分數 | 97.17% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏香港許可證與詳細的作用機轉資料。根據已知的藥理資訊，Tenapanor 是腸道局部作用的 NHE3 抑制劑，全身暴露極低，透過減少腸道鈉與磷的吸收發揮作用。

**坦白說，這個預測在機轉上缺乏支持。** NHE3 抑制與抗黴菌活性或念珠菌致病機轉之間，沒有已知的關聯。理論上，腸腔 pH 與鈉濃度改變可能影響黏膜菌叢，但這純屬推測。高分數很可能只是知識圖譜中的關聯性所致，並非生物學上的證據。

此外，排名前 10 的其他預測（如腎上腺功能不全、Stevens-Johnson 症候群、原發性皮膚 T 細胞淋巴瘤等）同樣缺乏機轉依據與證據。其中**克隆氏結腸炎 (Crohn's colitis)**（分數 94.29%）因藥物作用於腸道，生物學上相對合理，被標為「研究問題」，但 NHE3 抑制也可能加重腹瀉，僅適合前臨床探索。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68017 | IBSRELA TABLETS 50MG | 未載明 | 未載明 |

廠商：FOSUN INDUSTRIAL CO., LIMITED；狀態：有效（單方）。

---

## 安全性考量

- **藥物交互作用**：本次資料僅有藥理層面的標靶紀錄（鈉/氫交換體 3，NHE3），沒有具體的藥物間交互作用等級資訊。
- **其他提醒**：新藥本身也可能是 Stevens-Johnson 症候群的誘發因子，因此不宜在此類疾病中使用。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 念珠菌感染的預測僅來自模型，沒有臨床試驗或文獻，且機轉上找不到合理連結。
- 藥物全身吸收極低，難以在全身性或遠端部位達到有效濃度。

**若要推進需要：**
- 取得香港仿單（核准適應症、警語、禁忌症）與完整作用機轉資料
- 以體外實驗檢視 Tenapanor 對念珠菌生長或黏附的影響，確認是否有任何生物學訊號
- 若要探索腸道相關方向，可優先對克隆氏結腸炎進行前臨床研究，並特別評估腹瀉風險
- 在取得實質證據前，不建議進入臨床開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

