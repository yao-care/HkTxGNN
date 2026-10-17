---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 538
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Lopinavir：預測新適應症為貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)（證據等級 L5）。原適應症：HIV 感染、AIDS"
monitor_inn: "LOPINAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lopinavir：從 HIV 感染到貓後天免疫缺乏症候群

## 一句話總結

Lopinavir 是一種 HIV 蛋白酶抑制劑，原本用於 HIV 感染與 AIDS 的治療。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，但目前**沒有臨床試驗與文獻**直接支持這個預測，僅屬模型推論（證據等級 L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Lopinavir 是 HIV 蛋白酶抑制劑，在 HIV 感染中的療效已被證實。貓免疫缺乏病毒 (FIV) 與 HIV-1 同屬慢病毒，因此機轉上可能存在共同的蛋白酶標靶。

不過，FIV 的蛋白酶在受質特異性與對抑制劑的敏感度上都與 HIV-1 不同，交叉活性並不確定。0.999 的高分只是計算預測結果，沒有任何臨床試驗或文獻佐證。

另外值得注意，這個疾病是獸醫領域的適應症，對人類患者的藥物再利用價值有限。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

> 補充：排名第 2 的預測「猴免疫缺乏病毒 (SIV) 感染」有 3 篇獼猴前臨床研究（PMID 16973590、17350308、12951220），屬間接證據（L4）。因僅取得標題與摘要片段，無法確認每篇研究是否以 Lopinavir 為受試藥物。SIV 本身是 HIV 的動物模型，對人類的再利用價值同樣有限。排名第 3 的神經發展障礙預測，則未發現明確機轉關聯，不建議採信。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68129 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG（Chemill Pharma） | 未載明 | 未載明 |
| HK-65831 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG（Viatris） | 未載明 | 未載明 |
| HK-55200 | KALETRA TAB（AbbVie） | 未載明 | 未載明 |
| HK-66676 | LOPINAVIR AND RITONAVIR TABLETS USP 100MG/25MG（Controlled Medications） | 未載明 | 未載明 |
| HK-66612 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG（Hind Wing） | 未載明 | 未載明 |

（另有 KALETRA ORAL SOL，HK-48165，AbbVie，共 6 張有效許可證。）

---

## 安全性考量

- **主要警語與禁忌症**：香港仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。
- **知識圖譜中標示的禁忌或需謹慎的疾病**（非仿單文字）：
  - 心臟與心律：long QT 症候群、torsades de pointes、心臟傳導疾病、房室傳導阻滯、猝發性心臟停止、心肌缺血、冠狀動脈疾病、心肌病變
  - 肝膽胰：胰臟炎、肝病、肝硬化、膽囊疾病、慢性 B 型與 C 型肝炎
  - 代謝：高血糖、糖尿病、糖尿病酮酸中毒、高三酸甘油脂血症、低鉀血症、高膽紅素血症、Gilbert 症候群
  - 其他：血友病
- **藥物交互作用**：共 65 項，以下為部分：
  - 重大 (Major)：Dolasetron、Papaverine
  - 中度 (Moderate)：Acarbose、Dapagliflozin、Metformin、Levofloxacin、Ondansetron、Palonosetron、Famotidine，以及多種瀉劑（Bisacodyl、Lactulose 等）
  - 輕微 (Minor)：Cimetidine、Clotrimazole

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（貓免疫缺乏症候群）僅有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 疾病屬獸醫領域，且 FIV 與 HIV 蛋白酶存在差異，對人類的再利用價值有限。
- 藥物本身交互作用多（65 項），並涉及多項心臟與代謝禁忌。

**若要推進需要：**
- 取得 Lopinavir 的作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌症
- 驗證 Lopinavir 對 FIV 蛋白酶的體外抑制活性
- 確認排名第 2 之 SIV 相關研究是否確實以 Lopinavir 為受試藥物
- 先釐清此預測的目標族群（獸醫用途或人類用途），再決定是否值得投入
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

