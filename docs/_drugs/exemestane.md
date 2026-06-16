---
layout: default
title: Exemestane
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 5
---

# Exemestane
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

# Exemestane：從乳癌到先天性抗凝血酶缺乏症（Type 2）

## 一句話總結

Exemestane 是第三代芳香酶抑制劑（Aromatase Inhibitor, AI），原本用於停經後女性荷爾蒙受體陽性乳癌的輔助內分泌治療。TxGNN 模型預測它可能對**先天性抗凝血酶缺乏症 Type 2（Antithrombin Deficiency Type 2）** 等凝血相關疾病有效，但目前所有 5 項預測適應症均屬 **L5 等級**，無任何直接支持再利用的臨床試驗或文獻，且機轉分析揭示多項根本性缺陷。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未在香港取得上市許可；依藥理類別為停經後荷爾蒙受體陽性乳癌輔助內分泌治療 |
| 預測新適應症 | 先天性抗凝血酶缺乏症 Type 2（Antithrombin Deficiency Type 2） |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA [Data Gap]）。根據 Evidence Pack 內各適應症的機轉推論，Exemestane 為芳香酶抑制劑，透過**不可逆性抑制芳香酶（CYP19A1）**，阻斷雄激素轉化為雌激素，使全身雌激素水平顯著降低，已廣泛應用於乳癌輔助內分泌治療。

TxGNN 推斷的凝血關聯鏈為：Exemestane → 雌激素↓ → 促凝因子（Factor VIII、Fibrinogen）調控 → 對凝血異常疾病產生潛在保護效果。由於高雌激素狀態（如 Tamoxifen SERM 類藥物）確實與靜脈血栓風險上升有關，而 AI 類藥物血栓風險側寫相對較低，知識圖譜由此推斷可能存在治療潛力。

然而，**先天性抗凝血酶缺乏症 Type 2 是遺傳性蛋白質功能缺陷**，為 Antithrombin 蛋白功能位點突變所致。Exemestane 對 Antithrombin 蛋白的合成、表達或活性無任何已知直接作用。此機轉鏈結屬知識圖譜多跳共現推斷，間接性過高，**現階段無法建立合理的再利用科學基礎**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無針對第一預測適應症（先天性抗凝血酶缺乏症 Type 2）的相關文獻。

> **附註（第 2 預測適應症：閉經）**：Evidence Pack 中共有 5 篇文獻與「Exemestane + 閉經」相關，但機轉分析顯示這些文獻均在**乳癌合併卵巢抑制（OFS）**的治療框架下，討論 AI 類藥物**導致**化療誘發性閉經的發生率與可逆性——亦即 Exemestane 是閉經的**病因**，而非治療手段。此為因果方向倒置的典型 KG 推斷錯誤，文獻不支持再利用。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Prospective Cohort | Annals of Oncology | 乳癌患者由 Tamoxifen 換用 Exemestane 後，卵巢功能恢復（OFR）的發生率與預測因子 |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Systematic Review | Oncology (Williston Park) | 停經前早期乳癌卵巢抑制合併 Exemestane 之最佳輔助內分泌治療策略（SOFT/TEXT 試驗分析） |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Narrative Review | Recenti Progressi in Medicina | LHRH 類似物於停經前乳癌的角色；化療誘發閉經與卵巢抑制的臨床意義 |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Observational Study | J Clin Oncology | 乳癌卵巢抑制治療中雌二醇監測必要性的臨床評估 |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Review | Klinicka Onkologie | 停經後乳癌 AI 治療及副作用處置；說明 AI 類藥物於有功能性卵巢者為禁忌 |

---

## 香港上市資訊

Exemestane 目前**未在香港取得藥物登記**，無任何已核准的許可證記錄，無法提供香港核准適應症資訊。

---

## 細胞毒性

Exemestane 屬抗腫瘤藥物（芳香酶抑制劑），但為**非傳統細胞毒性的口服內分泌治療藥物**，與鉑類、紫杉醇等化療藥物性質不同。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（Endocrine Targeted Therapy）— 芳香酶抑制劑，非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 低（AI 類藥物通常不引起顯著骨髓抑制） |
| 致吐性分級 | 低 |
| 監測項目 | 骨密度（BMD）、血脂（LDL/HDL）、肝功能（ALT/AST）、雌二醇水平 |
| 處置防護 | 無需特殊細胞毒性藥物防護；一般口服製劑標準操作規範即可 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
全部 5 項 TxGNN 預測適應症均為 L5 等級，機轉審查揭示系統性問題：凝血相關預測（抗凝血酶缺乏、Factor V 過量、Heparin Cofactor II 缺乏、血栓形成傾向）屬知識圖譜多跳共現推斷，機轉鏈結間接性過高且對部分適應症可能呈**反向有害效果**（如 HCII 缺乏患者降低雌激素恐進一步削減 HCII 合成）；閉經預測則存在**因果方向倒置**——Exemestane 是閉經的病因，而非治療手段。在 Exemestane 未取得香港上市許可、且完全缺乏目標適應症直接臨床證據的情況下，不具備推進條件。

**若要推進需要：**
- 補充 Exemestane 完整 MOA 資料（查詢 DrugBank API，補足 DG002）
- 取得原廠仿單安全性資料（補足 DG001：警語、禁忌症）
- 針對「雌激素-凝血因子交互作用」進行系統性文獻回顧，確認是否存在直接治療潛力（而非間接環境調節）
- 重新審視 TxGNN 凝血相關節點的 KG 結構，評估是否為節點群集效應（Cluster Effect）造成的假陽性高分
- 若後續確認有再利用潛力並計畫在香港上市，需向衛生署藥物辦公室申請藥物登記
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

