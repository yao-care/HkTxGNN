---
layout: default
title: Benzoyl Peroxide
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Benzoyl Peroxide：從痤瘡到外陰倒置性毛囊角化症

## 一句話總結

Benzoyl Peroxide（過氧化苯甲醯，BPO）是國際上廣泛使用的外用抗痤瘡藥物，主要透過釋放活性氧自由基殺滅毛囊內細菌並促進角質溶解。
TxGNN 模型預測它可能對**外陰倒置性毛囊角化症（Vulvar Inverted Follicular Keratosis）**有效，
目前**無臨床試驗**及**無文獻**直接支持此預測方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痤瘡（Acne vulgaris，國際通用適應症） |
| 預測新適應症 | 外陰倒置性毛囊角化症（Vulvar Inverted Follicular Keratosis） |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Benzoyl Peroxide 是外用抗菌兼角質溶解藥物，透過釋放活性氧自由基（reactive oxygen species）殺滅毛囊皮脂腺單位中的 *Cutibacterium acnes*（前稱 *Propionibacterium acnes*），同時具有輕度角質溶解（keratolytic）活性，能疏通毛囊開口、抑制粉刺形成。其主要臨床應用集中於尋常性痤瘡的局部治療。

外陰倒置性毛囊角化症（Vulvar Inverted Follicular Keratosis, VIFK）是一種良性角化增生性病變，組織學上表現為毛囊漏斗部鱗狀上皮向內增生，伴有角化過度與「渦流細胞」（squamous eddies）。TxGNN 模型可能透過「毛囊發炎」與「角化異常」共享的知識圖譜節點，推斷 BPO 的角質溶解活性與 VIFK 的角化增生機轉存在生物學關聯性。

然而，此連結高度間接：VIFK 屬於良性腫瘤性病變，其病理驅動機轉（鱗狀上皮增生）與 BPO 的殺菌及角質溶解活性之間目前缺乏直接生物學依據。更重要的是，VIFK 病灶位於外陰黏膜-皮膚交界區，外用 BPO 於此部位的刺激性與安全性不能直接套用面部痤瘡的用藥經驗，需要獨立評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

Benzoyl Peroxide 在台灣目前**未取得藥品許可證**，無已上市品項資料可供參考。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖達 99.92%，但屬純模型推論（L5），目前完全缺乏臨床試驗或文獻直接支持 BPO 用於外陰倒置性毛囊角化症；病灶的良性腫瘤性病理機轉與 BPO 的抗菌/角質溶解活性之間尚無生物學連結，且病灶部位的局部安全性存在不確定性。

**若要推進需要：**
- 取得 BPO 完整作用機轉資料（DrugBank API 查詢）
- 取得台灣/國際仿單中的安全性警語與禁忌症（現為資料缺口）
- 前臨床研究評估 BPO 在外陰黏膜-皮膚區域的耐受性與刺激性
- 病理機轉文獻，確認角質溶解活性對 VIFK 是否具有治療潛力
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

