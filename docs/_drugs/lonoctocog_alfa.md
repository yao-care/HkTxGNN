---
layout: default
title: Lonoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 527
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
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

# Lonoctocog alfa：從 A 型血友病到偽性類血友病（pseudo-von Willebrand disease）

## 一句話總結

Lonoctocog alfa 是單鏈重組第八凝血因子（FVIII），一般用於 A 型血友病的凝血因子補充（香港許可證未附適應症文字，此為依藥物類別的判斷）。
TxGNN 模型預測它可能對**偽性類血友病 (pseudo-von Willebrand disease)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 偽性類血友病 (pseudo-von Willebrand disease) |
| TxGNN 預測分數 | 99.85%（排名 3598） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。已知 Lonoctocog alfa 是重組 FVIII，在凝血過程中作為 FIXa 的輔因子，參與 tenase 複合體。

偽性類血友病（血小板型 VWD）的根本缺陷在血小板 GPIbα 的功能增強。這會增加 VWF 結合，並加速清除高分子量 VWF 多聚體。VWF 與 FVIII 濃度可能因此繼發性下降，所以補充 FVIII 在理論上有一點依據，但這並未被證實。主要病灶在血小板，標準處置是輸注血小板或採用針對 VWF 的策略。

因此 99.85% 的高分數，較可能反映知識圖譜中「凝血與出血疾病」的鄰近關係，而非經驗證的機轉。

TxGNN 另外預測了三個適應症，同樣缺乏證據，機轉合理性更低：

| 排名 | 預測適應症 | 分數 | 機轉評估 |
|------|-----------|------|---------|
| 2 | 原發性血小板釋放障礙 | 99.84% | 缺陷在血小板顆粒釋放，補充 FVIII 無法矯正 |
| 3 | Glanzmann 血小板無力症 | 99.76% | 缺陷在 αIIbβ3 整合素，FVIII 本來正常，補充無益；標準治療為血小板輸注與重組 FVIIa |
| 4 | Scott 症候群 | 99.44% | 缺陷在血小板膜磷脂絲胺酸暴露，與 tenase 複合體有表面關聯，但病灶不是 FVIII 缺乏 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66199 | AFSTYLA 凍晶注射粉及溶劑 1000 IU | CSL Behring Asia Pacific Limited |
| HK-66200 | AFSTYLA 凍晶注射粉及溶劑 1500 IU | CSL Behring Asia Pacific Limited |
| HK-66201 | AFSTYLA 凍晶注射粉及溶劑 250 IU | CSL Behring Asia Pacific Limited |
| HK-66202 | AFSTYLA 凍晶注射粉及溶劑 500 IU | CSL Behring Asia Pacific Limited |

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢無結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 四個預測適應症都只有模型分數，沒有臨床試驗或文獻。
- 逐一檢視機轉後，補充 FVIII 都沒有明確的合理路徑，高分較可能是圖譜鄰近效應。

**若要推進需要：**
- 取得香港衞生署（Department of Health）核准仿單，補齊適應症、警語與禁忌症。
- 補齊 DrugBank 的作用機轉資料。
- 針對「偽性類血友病 + FVIII 補充」做系統性文獻檢索，確認是否有病例報告或機轉研究。
- 若文獻顯示有 FVIII 繼發性偏低的病例，再評估是否值得設計探索性研究。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

