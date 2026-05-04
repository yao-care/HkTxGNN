---
layout: default
title: Etonogestrel
parent: 中證據等級 (L3-L4)
nav_order: 252
evidence_level: L4
indication_count: 5
---

# Etonogestrel
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

# Etonogestrel：從避孕到閉經

## 一句話總結

Etonogestrel 是一種強效合成孕激素，目前以長效皮下植入劑（Nexplanon）形式廣泛用於避孕。
TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 具有治療潛力，
目前**無臨床試驗**及**文獻**直接支持，主要依賴機轉推論（證據等級 L4）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 避孕（長效皮下植入式） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Etonogestrel 是 desogestrel 的活性代謝物，屬第三代合成孕激素，透過與孕激素受體（PR-A/PR-B）高度結合，深度調控下丘腦-腦下垂體-卵巢軸（HPO 軸），同時抑制排卵、改變子宮內膜及子宮頸黏液性狀。

孕激素與閉經的關係具有「雙向機轉」值得關注：一方面，週期性孕激素給藥可誘發撤退性出血，用於治療無排卵性或低雌激素型繼發性閉經；另一方面，長效孕激素植入（如 Nexplanon）本身亦常以閉經作為預期效果，應用於子宮內膜異位症或異常子宮出血的長期管理。TxGNN 高分（0.998）正反映了孕激素受體與月經週期調控之間已確立的機轉關聯性。

需要注意的是，「治療閉經」與「誘發閉經」在臨床上必須依亞型嚴格區分。撤退性出血療法適用於繼發性閉經；而持續性高劑量孕激素給藥則可能維持閉經狀態，需結合閉經成因（下丘腦性、垂體性、子宮性等）進一步評估療效方向。

---

## 全部預測適應症概覽

本 Evidence Pack 包含 5 個 TxGNN 預測適應症，均屬婦科或乳腺激素相關病變：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|--------|-----------|---------|------|
| 1 | 閉經 (Amenorrhea) | 99.84% | L4 | Research Question |
| 2 | 乳腺纖維囊性病 (Breast Fibrocystic Disease) | 99.61% | L5 | Research Question |
| 3 | 乳腺鈍管腺病 (Blunt Duct Adenosis of Breast) | 99.29% | L5 | Hold |
| 4 | 乳腺頂泌腺腺病 (Apocrine Adenosis of Breast) | 99.29% | L5 | Hold |
| 5 | 乳腺良性發育不良 (Benign Mammary Dysplasia) | 99.21% | L5 | Research Question |

> ⚠️ **注意**：排名 3 與 4 的預測分數完全相同（0.9929），且 Evidence Pack 備註指出此可能為知識圖譜中相鄰節點的拓撲結構群聚效應（topological artifact），建議在後續分析中謹慎解讀，勿直接視為等效臨床適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（已查詢 ClinicalTrials.gov 及 ICTRP，所有 5 個預測適應症均未檢索到 Etonogestrel 相關試驗。）

---

## 文獻證據

目前無相關文獻。

（已查詢 PubMed，所有 5 個預測適應症均未檢索到 Etonogestrel 的直接相關文獻。）

---

## 香港上市資訊

Etonogestrel 在香港**尚未取得藥物登記**，許可證數為 0。

供參考：在香港以外的主要市場，Etonogestrel 以皮下植入劑形式（商品名 Nexplanon / Implanon NXT）已分別取得美國 FDA、歐盟 EMA 等機構核准，用於長效避孕。若考慮在香港進行臨床研究，需先就藥物登記狀態向衞生署進行諮詢。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
孕激素與閉經的機轉關聯在理論上合理（L4 等級），但目前完全缺乏 Etonogestrel 針對閉經或任何乳腺良性病變的直接臨床試驗及文獻支持；加之此藥在香港尚未上市，研究推進的起點門檻較高，建議先完成基礎資料補充再評估是否進入下一階段。

**若要推進需要：**
- 補充 Etonogestrel 完整作用機轉資料（建議查詢 DrugBank API，填補 DG002 資料缺口）
- 釐清目標閉經亞型（繼發性無排卵性為最合理切入點），確認孕激素治療方向
- 蒐集孕激素類效應文獻（如 medroxyprogesterone acetate、norethisterone 治療繼發性閉經的 RCT），作為 Etonogestrel 的間接類效應支撐
- 評估以閉經為目標效果（如子宮內膜異位症合併閉經）的潛在適應症場景，可能比「治療閉經」更具研究可行性
- 就香港藥物登記可行性向衞生署進行預諮詢
- 若考慮乳腺相關適應症（排名 2、5），建議優先以「乳腺良性發育不良」（排名 5）作為廣義切入，再逐步收窄至特定病理亞型
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

