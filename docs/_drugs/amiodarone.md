---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
last_modified_at: 2026-10-27
description: "Amiodarone：預測新適應症為兒茶酚胺敏感性多形性室性心搏過速 (catecholaminergic polymorphic ventricular tachycardia)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Amiodarone
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

## Amiodarone：抗心律不整藥物（多重離子通道阻斷劑） → 兒茶酚胺敏感性多形性室性心搏過速 (catecholaminergic polymorphic ventricular tachycardia)
{: .text-alpha }

## 一句話總結

Amiodarone 是一種多重離子通道阻斷型抗心律不整藥物。
TxGNN 模型預測它可能對**兒茶酚胺敏感性多形性室性心搏過速 (catecholaminergic polymorphic ventricular tachycardia)** 有效，
但目前**沒有相關臨床試驗**，文獻僅有 9 篇（世代研究、回顧與病例報告），且沒有任何一篇以 amiodarone 作為此疾病的主要治療進行評估。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 兒茶酚胺敏感性多形性室性心搏過速 (catecholaminergic polymorphic ventricular tachycardia) |
| TxGNN 預測分數 | 0.9978 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠機轉欄位未收錄）。就藥理類別而言，amiodarone 屬多重離子通道阻斷劑，可作用於鉀、鈉、鈣通道及 β 腎上腺素受體，理論上可能抑制由兒茶酚胺誘發的心室性心律不整。

然而，CPVT 的病理核心是 RYR2 或 CASQ2 突變造成的舒張期鈣離子滲漏。目前公認的治療是 β 阻斷劑與 flecainide，amiodarone 一般被認為療效不足或不如前述藥物。因此，模型的高分預測在機轉上僅有部分合理性，不能視為療效證據。

所提供的文獻多為 CPVT 的族群描述、藥物治療回顧與個案報告，並未直接評估 amiodarone 作為此疾病的治療，故證據上只能視為模型預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | 回顧心室性心律不整的藥物治療進展，抗心律不整藥物仍是急性轉復與長期預防的重要手段 |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | 系統性回顧 | Life (Basel) | 整理中國 CPVT 患者的臨床特徵、基因發現與心律不整結果 |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | 世代研究 | Rev Cardiovasc Med | 描述中國城市 CPVT 患者的臨床特徵、基因基礎、醫療資源使用與費用 |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | 病例報告 | Pacing Clin Electrophysiol | Flecainide 抑制 CPVT 患者植入式去顫器引起的風暴 |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | 病例報告 | Turk Pediatri Arsivi | 2 歲男童以心搏驟停表現的 CPVT |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | 病例報告 | Medicine | 9 歲兒童 RYR2 突變 CPVT，延遲診斷 6 年 |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | 病例報告 | Front Cardiovasc Med | 青少年 CPVT 在左側後再行右側心臟交感神經切除而緩解 |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | 病例報告 | BMJ Case Rep | 幼童院外心搏驟停，反覆室性心搏過速／心室顫動的診斷難題 |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | 病例報告 | Anesth Analg | 長 QT 症候群新生兒，使用 lidocaine、esmolol 與 amiodarone 處理難治性心律不整 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27296 | CORDARONE INJECTABLE SOLUTION 0.15G/3ML | 未記錄 | 未記錄 |
| HK-66829 | AMIODARONE RIVOPHARM TABLETS 200MG | 未記錄 | 未記錄 |
| HK-27294 | CORDARONE TAB 200MG | 未記錄 | 未記錄 |
| HK-65597 | AMIODARONE GP TABLETS 200MG | 未記錄 | 未記錄 |
| HK-60895 | AMIODARONE SANDOZ TAB 200MG | 未記錄 | 未記錄 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共 100 筆交互作用紀錄，其中重大（Major）等級包括 cisapride、clarithromycin、clotrimazole、dolasetron、eliglustat、hydrocortisone、dexamethasone、agalsidase beta 及多種 amphotericin B 製劑。
- **需特別留意的疾病背景**：本報告所用資料中，與 amiodarone 相關的禁忌或需謹慎的情況包括長 QT 症候群、尖端扭轉型心搏過速、房室傳導阻滯、病態竇房症候群、甲狀腺功能低下或亢進、肝臟疾病、間質性肺病、視神經炎及周邊神經病變等。這些並非仿單文字，正式禁忌症請以原廠仿單為準。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測沒有任何臨床試驗支持，文獻也未直接評估 amiodarone 用於 CPVT，證據等級為 L5。
- CPVT 已有 β 阻斷劑與 flecainide 等較確立的治療，amiodarone 被認為療效不足，且其肺、甲狀腺、肝臟毒性與 QT 延長風險不容忽視。

**若要推進需要：**
- 取得 amiodarone 在 CPVT 的直接臨床或前臨床數據（例如 RYR2／CASQ2 模型中的抗心律不整效果）
- 與 β 阻斷劑、flecainide 的比較性證據
- 補齊作用機轉資料與香港仿單的警語及禁忌症
- 針對兒童及年輕患者的長期安全性評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

