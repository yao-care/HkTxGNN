---
layout: default
title: Flubendazole
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Flubendazole
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

# Flubendazole：從驅腸蟲到膀胱癌

## 一句話總結

Flubendazole 是苯並咪唑（benzimidazole）類驅腸蟲藥，透過抑制微管蛋白聚合發揮療效。TxGNN 模型預測它可能對**膀胱癌（Urinary Bladder Carcinoma）** 有效，然而目前**無任何直接臨床試驗**，僅有 **1 篇以同族藥 fenbendazole 為研究對象的前臨床文獻**提供間接機轉類比依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腸道寄生蟲感染（苯並咪唑類驅腸蟲藥） |
| 預測新適應症 | 膀胱癌（Urinary Bladder Carcinoma） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅模型預測，無直接 Flubendazole 癌症研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Flubendazole 屬苯並咪唑類藥物，其理論抗腫瘤機轉為抑制 β-tubulin 聚合，干擾有絲分裂紡錘體形成，誘導腫瘤細胞停滯於 G2/M 期並觸發凋亡。此機轉與紫杉醇、長春花鹼類等抗微管藥物類似，理論上對快速增殖的癌細胞具有抑制潛力。**然而，目前缺乏任何直接針對 Flubendazole 本身用於癌症的體外或體內研究。**

TxGNN 前 10 名預測全數集中於膀胱相關腫瘤（分數 99.98–99.99%），反映知識圖譜中 Flubendazole 節點與膀胱腫瘤節點之間存在強連結。值得注意的是，排名 8–10 的三個罕見膀胱腺癌亞型（colonic type、colloid、mixed）TxGNN 分數完全相同（0.9998492），強烈暗示這些亞型在知識圖譜中共用相同節點，預測結果缺乏亞型特異性，需謹慎解讀。

最具參考價值的間接佐證來自同族藥 **fenbendazole**（PMID 39128990）——該研究顯示 fenbendazole 膀胱內灌注結合 CRISPR-Cas13a 對膀胱癌有協同抗腫瘤活性。Flubendazole 口服生物利用度雖較低，但**膀胱內灌注**給藥模式可直接接觸膀胱上皮腫瘤細胞，理論上可繞過系統性吸收限制。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

> ⚠️ 以下文獻研究對象為同族藥 **fenbendazole**，非 Flubendazole 直接證據，僅供機轉類比參考。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | Preclinical (in vitro + in vivo) | Journal of Experimental & Clinical Cancer Research | Fenbendazole 結合 CRISPR-Cas13a 進行膀胱內灌注，對膀胱癌顯示協同抗腫瘤活性；該系統尚屬實驗性階段 |

---

## 香港上市資訊

Flubendazole 在香港目前**未取得上市許可**，無任何許可證記錄。如需取得此藥，需透過特殊進口或研究用途申請管道。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前證據等級為 L5，無任何直接針對 Flubendazole 用於膀胱癌的研究。唯一相關文獻為同族藥 fenbendazole 的前臨床研究，機轉類比尚不足以支持進入臨床評估。加之 Flubendazole 在香港未上市，藥物可及性亦構成實際障礙。

**若要推進需要：**
- 補充 Flubendazole 完整作用機轉資料（DrugBank MOA、toxicity profile）
- 進行 Flubendazole 針對膀胱癌細胞株的體外細胞毒性試驗（IC50、細胞凋亡確認）
- 評估膀胱內灌注劑型可行性（溶解度、穩定性、刺激性）
- 補充安全性資訊（原廠仿單警語、禁忌症、藥物交互作用）
- 確認是否存在針對 benzimidazole 類藥物更廣泛的膀胱癌前臨床數據可供類比
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

